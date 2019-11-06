#!/bin/bash
# Call from root of project:
#   ./scripts/update-all-message-urls.sh

find . -type f -name '*.md' -exec sh -c '
  for file do
    echo "Updating $file ..."
    cat "$file" | ./scripts/apply-message-urls.sh > "$file".updated && mv "$file".updated "$file"
  done
' sh {} +
