#!/bin/bash
# script that makes a request and receives a message
curl -sL -X PUT -H "Origin: NewSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
