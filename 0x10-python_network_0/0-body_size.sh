#!/bin/bash
# script that takes url, sends a request
# and displays size of the body of the response

curl -sI "$1" | grep 'Content-length' | awk '{print $2}'