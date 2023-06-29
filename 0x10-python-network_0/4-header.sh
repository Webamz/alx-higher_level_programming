#!/bin/bash
# takes in a URL as an argument, sneds a GET request 
# and displays the body of the response
curl -sH "X-School-User_Id: 98" "$1"