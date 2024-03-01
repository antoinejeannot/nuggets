#!/bin/bash

mkdir -p pdf

for file in markdown/*.md; do
    filename=$(basename -- "$file")
    filename="${filename%.*}"
    title=$(echo $filename | tr '_' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1' | sed 's/ And / \& /g')
    pandoc \
        --from markdown \
        --to pdf \
        --toc \
        --highlight-style=tango \
        "$file" \
        -o "pdf/$filename.pdf" \
        --toc-depth=2 \
        --metadata \
        title="$title" \
        --css bin/pandoc.css
    echo "Converted $file -> pdf/$filename.pdf"
done