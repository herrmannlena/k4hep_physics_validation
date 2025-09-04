# move_root_files.sh
# Usage: source move_root_files.sh

# Define output directory
OUTPUT_DIR="../output_data"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Move .root files to output_data
mv -- *.root "$OUTPUT_DIR" 2>/dev/null

# Feedback
echo "Moved .root files to $OUTPUT_DIR/"
cd ..
