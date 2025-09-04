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
