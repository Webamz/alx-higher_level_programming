#!/bin/bash
# takes url, sends request and displays the body

curl -s "$1" -X GET -L