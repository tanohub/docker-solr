# https://gist.github.com/CesarCapillas/a796c0e7cba10ac02213c7f3485d6e90

SERVER=${1:-localhost}
PORT=${2:-8983}
NUMSERVERS=${3:-1}

if [ "$PORT" = "443" ]; then
   PROTOCOL="https"
else
   PROTOCOL="http"
fi

ENDPOINT="$PROTOCOL://${SERVER}:${PORT}/solr/admin/collections?action=clusterstatus&wt=json"

if [[ "$1" == "" ]]; then
  echo "Usage:"
  echo "  check_solr.sh <SOLRSERVER=localhost> [<PORT=8983> <NUMSERVERS=1>]"
  exit
fi

CURL=`curl --silent -X GET ${ENDPOINT}`
CHCK=`echo $CURL | grep "live_nodes"`
if [[ "$CHCK" == "" ]]; then
   CHECK="Failed"
else
   CHECK="OK"
   #SOLR_RES=`echo $CURL | jq ".cluster.live_nodes" | tr -d '\r\n'`
   SOLR_RES=`echo $CURL | jshon -e cluster | jshon -e live_nodes | tr -d '\r\n'`
   # tricky
   #SOLR_RES=`echo $CURL | jq ".cluster.live_nodes" | wc -w`
   SOLR_NUM=`echo $CURL | jshon -e cluster | jshon -e live_nodes | wc -w`
   SOLR_VAR=`expr $SOLR_NUM - 2`
fi

if [[ "$CHECK" == "OK" ]]; then
   if (($SOLR_VAR < $NUMSERVERS));then
      echo "CRITICAL: SOLR ($SOLR_VAR live nodes) = $SOLR_RES (<$NUMSERVERS)"
      exit 2
   fi
   echo "INFO: SOLR ($SOLR_VAR live nodes) = $SOLR_RES "
   exit 0
elif [[ "$CHECK" == "Failed" ]]; then
   echo "CRITICAL: ${SERVER}"
   exit 2
else
   echo "Check failed."
   exit 3
fi
