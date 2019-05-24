#!/bin/bash

mkdir -p --mode=777 /tmp/sample_data/random
mkdir -p --mode=777 /tmp/sample_data/small
mkdir -p --mode=777 /tmp/sample_data/large

curl http://ipv4.download.thinkbroadband.com/20MB.zip --output "/tmp/sample_data/random/20MB.zip"
curl https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.A1.png --output "/tmp/sample_data/random/250MBb.png"
curl https://www.briandunning.com/sample-data/us-500.zip --output "/tmp/sample_data/random/small.csv"
curl http://ipv4.download.thinkbroadband.com/1GB.zip --output "/tmp/sample_data/random/1GB.zip"
curl http://ipv4.download.thinkbroadband.com/512MB.zip --output "/tmp/sample_data/random/500MB.zip"
curl http://ipv4.download.thinkbroadband.com/200MB.zip --output "/tmp/sample_data/random/200MB.zip"
curl http://ipv4.download.thinkbroadband.com/100MB.zip --output "/tmp/sample_data/random/100MB.zip"
curl https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.D2.png --output "/tmp/sample_data/random/250MBa.png"

# TODO: Generate files for Small Test Case
# TODO: Generate files for Large Test Case
