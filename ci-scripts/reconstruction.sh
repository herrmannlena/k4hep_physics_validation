cd "${CLDCONFIG}/share/CLDConfig"
echo "RECONSTRUCTION PHASE:"
k4run CLDReconstruction.py \
    --inputFiles "${WORKAREA}/${OUTFILEBASE}_SIM.root" \
    --outputBasename "${WORKAREA}/${OUTFILEBASE}" 

cd "${WORKAREA}"

echo "Reconstruction was successful!"
cd $WORKAREA
