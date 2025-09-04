echo "TAGGING PHASE:"
k4run "${TAGGERSTEERING}" \
        --inputFiles "${WORKAREA}/${OUTFILEBASE}_REC.edm4hep.root" \
        --outputFile "${WORKAREA}/${OUTFILEBASE}_TAGGER.root"
