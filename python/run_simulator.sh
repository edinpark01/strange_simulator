#!/bin/bash

source /simulator/venv/bin/activate
python /simulator/run_simulator.sh ${ACCESS_KEY} ${SECRET_KEY} ${REGION} ${BUCKET_NAME}
deactivate

