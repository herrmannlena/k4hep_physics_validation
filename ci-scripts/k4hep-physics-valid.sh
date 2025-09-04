# First iteration of a script to be used for physics validation in the reco/sim pipeline with key4hep 
# uses CLD as example for now 
# tester events: wzp6_ee_mumuH_ecm240_GEN.stdhep # TO BE REPLACED 

#some fixed variables for now:
NUMBER_OF_EVENTS=1000

# enable exit on error to check correct script execution from within pipeline
set -e

# setup phase
echo "Setting up software stack"
# only source the setup if it is not set up yet
[ -z "$KEY4HEP_STACK" ] && source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh

echo "Downloading necessary Github repos..."
git clone https://github.com/key4hep/k4geo.git
K4GEO_PATH=$(realpath k4geo)
echo "Downloads finished"

# # simulation phase
echo "SIMULATION PHASE:"

# cd "${CLDCONFIG}/share/CLDConfig"
echo "Starting simulation..."

ddsim --steeringFile "${CLDCONFIG}/share/CLDConfig/cld_steer.py" \
      --compactFile "${K4GEO}/FCCee/CLD/compact/CLD_o2_v07/CLD_o2_v07.xml" \
      --numberOfEvents "${NUMBER_OF_EVENTS}" \
      --inputFiles ../data/wzp6_ee_mumuH_ecm240_GEN.stdhep
      --outputFile "${WORKAREA}/${GEOMETRY}/${VERSION}/ARC_sim.root" \
      --random.enableEventSeed --random.seed 42 \
      --part.userParticleHandler="" > "${WORKAREA}/${GEOMETRY}/${VERSION}/ddsim_log.txt"
echo "Simulation execution finished"


# get the CLD config repository
git clone https://github.com/key4hep/CLDConfig.git
cd CLDConfig/CLDConfig
# retrieve Z(mumu)H(X) MC generator events
wget https://fccsw.web.cern.ch/fccsw/tutorials/MIT2024/wzp6_ee_mumuH_ecm240_GEN.stdhep.gz
gunzip wzp6_ee_mumuH_ecm240_GEN.stdhep.gz
# run the Geant4 simulation
ddsim -I wzp6_ee_mumuH_ecm240_GEN.stdhep -N 10 -O wzp6_ee_mumuH_ecm240_CLD_SIM.root 
# NB: we run only on 10 events (-N 10) here for the sake of time
# for such small amount of event the detector geometry construction step dominates, it takes about 5 seconds per event and the geometry loading takes 1min30s

# # simulation phase
# echo "SIMULATION PHASE:"

# cd "${CLDCONFIG}/share/CLDConfig"
# echo "Starting simulation..."
# ddsim --steeringFile cld_arc_steer.py \
#       --compactFile "${K4GEO_PATH}/test/compact/ARC_standalone_o1_v01.xml" \
#       --enableGun --gun.distribution "cos(theta)" \
#       --gun.energy "20*GeV" --gun.particle proton \
#       --numberOfEvents "${NUMBER_OF_EVENTS}" \
#       --outputFile "${WORKAREA}/${GEOMETRY}/${VERSION}/ARC_sim.root" \
#       --random.enableEventSeed --random.seed 42 \
#       --part.userParticleHandler="" > "${WORKAREA}/${GEOMETRY}/${VERSION}/ddsim_log.txt"
# echo "Simulation execution finished"

# cd "${WORKAREA}/${GEOMETRY}/${VERSION}"


# # analyze simulation file
# echo "ANALYSIS PHASE:"

# echo "Starting analysis script..."
# python "${WORKAREA}/key4hep-reco-validation/scripts/FCCee/CLD/ARC_make_hists.py" \
#        -f ARC_sim.root -o results.root \
#        -c "${K4GEO_PATH}/test/compact/ARC_standalone_o1_v01.xml"
# echo "Analysis execution finished"