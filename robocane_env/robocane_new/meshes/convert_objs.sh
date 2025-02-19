#!/bin/bash

# Directories for input OBJ files and output STL files.
INPUT_DIR="obj/"
OUTPUT_DIR="stl/"

# Create the output directory if it doesn't exist.
mkdir -p "$OUTPUT_DIR"

# Loop through each OBJ file in the input directory.
for obj_file in "$INPUT_DIR"/*.obj; do
    # Extract the base file name without extension.
    base_name=$(basename "$obj_file" .obj)
    output_file="$OUTPUT_DIR/${base_name}.stl"
    
    echo "Converting: $obj_file → $output_file"
    
    # Convert using meshlabserver.
    meshlabserver -i "$obj_file" -o "$output_file" -m vc vn
done

echo "Batch conversion complete!"

