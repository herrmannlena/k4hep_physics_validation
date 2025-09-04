source ./config.cfg

WORKAREA=$PWD
INFILENAME="${WORKAREA}/../data/${INPUTPROCESS}_GEN.stdhep"
OUTFILEBASE="TEST_${INPUTPROCESS}_$(date +%Y%m%d)"


[ -z "$KEY4HEP_STACK" ] && source KEY4HEP_SETUP
