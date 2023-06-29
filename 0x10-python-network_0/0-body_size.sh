#!/bin/bash
# response of byte size
curl -s "$1" | wc -c
