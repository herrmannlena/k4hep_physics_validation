# First iteration of a script to be used for physics validation in the reco/sim pipeline with key4hep 
# uses CLD as example for now 
# tester events: wzp6_ee_mumuH_ecm240_GEN.stdhep # TO BE REPLACED 

#some fixed variables for now:
NUMBER_OF_EVENTS=10
WORKAREA=$PWD
INFILEBASE="wzp6_ee_mumuH_ecm240_GEN"
INFILENAME="${INFILEBASE}.stdhep"
OUTFILENAME="tester_${INFILENAME}_$(date +%Y%m%d).root"

# enable exit on error to check correct script execution from within pipeline
set -e

# setup phase
echo "Setting up software stack"
# only source the setup if it is not set up yet
[ -z "$KEY4HEP_STACK" ] && source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh

# is this necessary ? 
# echo "Downloading necessary Github repos..."
# git clone https://github.com/key4hep/k4geo.git
# K4GEO_PATH=$(realpath k4geo)
# echo "Downloads finished"

# # simulation phase
echo "SIMULATION PHASE:"

# cd "${CLDCONFIG}/share/CLDConfig"
echo "Starting simulation..."

ddsim --steeringFile "${CLDCONFIG}/share/CLDConfig/cld_steer.py" \
      --compactFile "${K4GEO}/FCCee/CLD/compact/CLD_o2_v07/CLD_o2_v07.xml" \
      --numberOfEvents "${NUMBER_OF_EVENTS}" \
      --inputFiles ../data/${INFILENAME} \
      --outputFile "${WORKAREA}/${OUTFILENAME}" 

echo "Simulation execution finished"


# cd "${WORKAREA}/${GEOMETRY}/${VERSION}"


# # analyze simulation file
# echo "ANALYSIS PHASE:"

# echo "Starting analysis script..."
# python "${WORKAREA}/key4hep-reco-validation/scripts/FCCee/CLD/ARC_make_hists.py" \
#        -f ARC_sim.root -o results.root \
#        -c "${K4GEO_PATH}/test/compact/ARC_standalone_o1_v01.xml"
# echo "Analysis execution finished"