#!/bin/bash
# Scriptt that sends a JSON post request to a URL passed as the first argument and displays the body of the response
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
