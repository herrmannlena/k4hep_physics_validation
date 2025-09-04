cd "${CLDCONFIG}/share/CLDConfig"
echo "RECONSTRUCTION PHASE:"
k4run CLDReconstruction.py \
    --inputFiles "${WORKAREA}/${OUTFILEBASE}_SIM.root" \
    --outputBasename "${WORKAREA}/${OUTFILEBASE}" \
    --num-events -1 \
    --enableLCFIJet 
cd "${WORKAREA}"

echo "Reconstruction was successful!"
cd $WORKAREA
