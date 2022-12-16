#!/bin/bash
# sends a DELETE request to the URL passed
curl -sI "$1" | grepe "Allow" | cut -d " " -f 2-
