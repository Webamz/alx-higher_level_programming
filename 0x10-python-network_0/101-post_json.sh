#!/bin/bash
# sends a JSON POST request to a URL passed as first argument
# and displays body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2"