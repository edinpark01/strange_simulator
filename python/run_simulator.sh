#!/bin/bash

access_key=$1
secret_key=$2
region=$3
bucket_name=$4

source /simulator/venv/bin/activate
python /simulator/run_simulator.sh ${access_key} ${secret_key} ${region} ${bucket_name}
deactivate

