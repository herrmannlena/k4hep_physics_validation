# # simulation phase
echo "SIMULATION PHASE:"

# cd "${CLDCONFIG}/share/CLDConfig"
echo "Starting simulation..."
cd "${CLDCONFIG}/share/CLDConfig"
ddsim --steeringFile cld_steer.py \
       --compactFile "${K4GEO}/FCCee/CLD/compact/CLD_o2_v07/CLD_o2_v07.xml" \
       --numberOfEvents "${NUMBER_OF_EVENTS}" \
       --inputFiles "${INFILENAME}" \
       --outputFile "${WORKAREA}/${OUTFILEBASE}_SIM.root" 

echo "Simulation execution finished"
