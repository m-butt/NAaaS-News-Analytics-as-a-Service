#!/bin/bash

dockerfile_path="$(pwd)/Dockerfile"  # Dockerfile in the current directory

# Check if the Dockerfile exists
if [[ ! -f "$dockerfile_path" ]]; then
  echo "Dockerfile not found: $dockerfile_path"
  exit 1
fi

# Read the Dockerfile line by line
while IFS= read -r line; do
  # Replace occurrences of './NAaaS/Spark/' with '.'
  modified_line="${line//\.\/NAaaS\/Spark\//.}"
  
  # Print the modified line
  echo "$modified_line"
done < "$dockerfile_path"
