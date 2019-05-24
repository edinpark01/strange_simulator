#!/bin/bash
source venv/bin/activate
unset HTTP_PROXY
unset HTTPS_PROXY
unset http_proxy
unset https_proxy

#python python/simulator.py --platform cohesity --bucket-name test-s3

deactivate