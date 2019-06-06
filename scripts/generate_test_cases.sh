#!/bin/bash
echo "=> Creating temporary folders"
[[ ! -d /tmp/sample_data/random ]] \
         && mkdir -p /tmp/sample_data/random \
         && chmod 755 /tmp/sample_data/random \
         || echo "Folder already created"
[[ ! -d /tmp/sample_data/small ]] \
    && mkdir -p /tmp/sample_data/small \
    && chmod 755 /tmp/sample_data/small \
    || echo "Folder already created"
[[ ! -d /tmp/sample_data/large ]] \
    && mkdir -p /tmp/sample_data/large \
    && chmod 755 /tmp/sample_data/large \
    || echo "Folder already created"

echo
echo "=> Downloading test files"
if [ ! -f "/tmp/sample_data/random/20MB.zip" ]; then
    curl http://ipv4.download.thinkbroadband.com/20MB.zip --output "/tmp/sample_data/random/20MB.zip"
else
    echo "Already downloaded - random/20MB.zip"
fi

if [ ! -f "/tmp/sample_data/random/250MBb.png" ]; then
    curl https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.A1.png --output "/tmp/sample_data/random/250MBb.png"
else
    echo "Already downloaded - random/250MBb.png"
fi

if [ ! -f "/tmp/sample_data/random/small.csv" ]; then
    curl https://www.briandunning.com/sample-data/us-500.zip --output "/tmp/sample_data/random/small.csv"
else
    echo "Already downloaded - random/small.csv"
fi

if [ ! -f "/tmp/sample_data/random/1GB.zip" ]; then
    curl http://ipv4.download.thinkbroadband.com/1GB.zip --output "/tmp/sample_data/random/1GB.zip"
else
    echo "Already downloaded - random/1GB.zip"
fi

if [ ! -f "/tmp/sample_data/random/500MB.zip" ]; then
    curl http://ipv4.download.thinkbroadband.com/512MB.zip --output "/tmp/sample_data/random/500MB.zip"
else
    echo "Already downloaded - random/500MB.zip"
fi

if [ ! -f "/tmp/sample_data/random/200MB.zip" ]; then
    curl http://ipv4.download.thinkbroadband.com/200MB.zip --output "/tmp/sample_data/random/200MB.zip"
else
    echo "Already downloaded - random/200MB.zip"
fi

if [ ! -f "/tmp/sample_data/random/100MB.zip" ]; then
    curl http://ipv4.download.thinkbroadband.com/100MB.zip --output "/tmp/sample_data/random/100MB.zip"
else
    echo "Already downloaded - random/100MB.zip"
fi

if [ ! -f "/tmp/sample_data/random/250MBa.png" ]; then
    curl https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.D2.png --output "/tmp/sample_data/random/250MBa.png"
else
    echo "Already downloaded - random/250MBa.png"
fi

# TODO: Generate files for Small Test Case
# TODO: Generate files for Large Test Case
