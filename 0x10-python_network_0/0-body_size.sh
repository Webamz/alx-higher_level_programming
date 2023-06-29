#!/bin/bash
# script that takes url, sends a request
# and displays size of the body of the response

curl -sI "$1" | grep 'Content-Length' | cut -d " " -f 2