#!/bin/bash
# script that displays all https methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
