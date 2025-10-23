#!/bin/bash

# Script to format MDX files using dprint
# Usage: ./format-mdx.sh <file.mdx>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <file.mdx>"
    exit 1
fi

MDX_FILE="$1"
MD_FILE="${MDX_FILE%.mdx}.md"

# Check if file exists
if [ ! -f "$MDX_FILE" ]; then
    echo "Error: File $MDX_FILE not found"
    exit 1
fi

# Copy MDX to MD temporarily
cp "$MDX_FILE" "$MD_FILE"

# Format with dprint
dprint fmt "$MD_FILE"

# Copy formatted content back to MDX
cp "$MD_FILE" "$MDX_FILE"

# Clean up temporary MD file
rm "$MD_FILE"

echo "Formatted $MDX_FILE"
