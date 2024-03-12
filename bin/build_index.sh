#!/bin/bash

output="html/index.html"
mkdir -p html
pandoc \
    --from markdown \
    --to html5 \
    --standalone \
    --embed-resources \
    --highlight-style=tango \
    "README.md" \
    -o $output \
    --metadata \
    title="" \
    --css bin/pandoc.css
python bin/add_analytics.py $output /nuggets/index.html
echo "Converted README.md -> $output"