#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response (no pipe, redirection, ;, && nk)
curl -so /dev/null -w "%{http_code}" "$1"
