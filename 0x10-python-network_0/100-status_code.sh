#!/bin/bash
# script that sends get request & display response
curl -s -o /dev/null -w "%{http_code}" "$1"
