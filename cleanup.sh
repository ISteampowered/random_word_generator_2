#!/usr/bin/env bash
# sed -i -n '/End of the Project Gutenberg EBook/q;p' $1      # removes everything after "End of the project..."
# sed -i -n '/^FOOTNOTES: /q;p' $1                            # removes everything after "FOOTNOTES"
# sed -i '/START OF THIS PROJECT GUTENBERG EBOOK /,$!d' $1    # removes everything before "START OF THIS..."
sed -i 's/[^a-z ]/ /gI' $1                                  # removes everything but letters and spaces
sed -i 's/ \+/ /g' $1                                       # truncates whitespace