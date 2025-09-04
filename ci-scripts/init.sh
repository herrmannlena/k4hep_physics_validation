source config.cfg

echo "SETUP PHASE:"
# only source the setup if it is not set up yet
[ -z "$KEY4HEP_STACK" ] && source "$KEY4HEP_SETUP"

