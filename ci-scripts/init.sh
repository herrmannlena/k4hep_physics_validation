source ./config.cfg

# Debugging info
echo "Using Key4HEP setup: $KEY4HEP_SETUP"
echo "Working area: $WORKAREA"
echo "Input: $INFILENAME"
echo "Output: $OUTFILENAME"

set -e

# setup phase
echo "Setting up software stack"
[ -z "$KEY4HEP_STACK" ] && source "$KEY4HEP_SETUP"
