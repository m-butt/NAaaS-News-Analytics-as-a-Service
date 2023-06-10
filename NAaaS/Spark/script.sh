#!/bin/bash

dockerfile_path="$(pwd)/Dockerfile"  # Dockerfile in the current directory
temp_file_path="$(pwd)/temp.dockerfile"  # Temporary file to store modifications

# Check if the Dockerfile exists
if [[ ! -f "$dockerfile_path" ]]; then
  echo "Dockerfile not found: $dockerfile_path"
  exit 1
fi

# Copy Dockerfile to temporary file
cp "$dockerfile_path" "$temp_file_path"

# Modify the Dockerfile line by line
while IFS= read -r line; do
  # Replace occurrences of './NAaaS/Spark/' with './'
  modified_line="${line//\.\/NAaaS\/Spark\//.\/}"
  
  # Append the modified line to the temporary file
  echo "$modified_line" >> "$temp_file_path"
done < "$dockerfile_path"

# Replace the original Dockerfile with the modified file
mv "$temp_file_path" "$dockerfile_path"

echo "Dockerfile has been modified."
