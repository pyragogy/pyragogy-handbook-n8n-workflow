#!/bin/bash
# Script to load sample data into the database or trigger sample workflow runs.

# Example:
# echo "Loading sample data..."
# curl -X POST \
#   http://localhost:5678/webhook/pyragogy/process \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "title": "Sample Handbook Entry",
#     "text": "This is a sample text for the handbook.",
#     "tags": ["sample", "test"],
#     "requireHitl": true
#   }'
# echo "Sample workflow initiated."
