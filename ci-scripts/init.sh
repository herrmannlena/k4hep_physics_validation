source config.cfg
echo
echo "CONFIGURATION:"
echo "  KEY4HEP_SETUP   = $KEY4HEP_SETUP"
echo "  NUMBER_OF_EVENTS= $NUMBER_OF_EVENTS"
echo "  WORKAREA        = $WORKAREA"
echo "  INPUTPROCESS    = $INPUTPROCESS"
echo "  INFILENAME      = $INFILENAME"
echo "  OUTFILEBASE     = $OUTFILEBASE"
echo
echo "SETUP PHASE:"
# only source the setup if it is not set up yet
[ -z "$KEY4HEP_STACK" ] && source "$KEY4HEP_SETUP"

