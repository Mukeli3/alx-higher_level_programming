#!/bin/bash
#  takes in a URL, sends a GET request to the URL, and displays the body of the response (only 200 status code response body displayed)
curl -sL "$1"
