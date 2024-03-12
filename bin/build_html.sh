#!/bin/bash

mkdir -p html

for file in markdown/*.md; do
    filename=$(basename -- "$file")
    filename="${filename%.*}"
    title=$(echo $filename | tr '_' ' ' | awk '{for(i=1;i<=NF;i++)sub(/./,toupper(substr($i,1,1)),$i)}1' | sed 's/ And / \& /g')
    sed '/# skip test/d' $file > $file.tmp.md
    pandoc \
        --from markdown \
        --to html5 \
        --standalone \
        --embed-resources \
        --toc \
        --highlight-style=tango \
        "$file.tmp.md" \
        -o "html/$filename.html" \
        --toc-depth=2 \
        --metadata \
        title="$title" \
        --css bin/pandoc.css
    rm $file.tmp.md
    python bin/collapse_details.py "html/$filename.html"
    python bin/add_analytics.py "html/$filename.html" /nuggets/$filename.html
    python bin/add_comments.py "html/$filename.html"
    echo "Converted $file -> html/$filename.html"
done