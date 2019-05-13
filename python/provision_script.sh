#!/usr/bin/env bash

access_key=$1
secret_key=$2
region=$3
bucket_name=$4

sudo yum install -y wget python3

mkdir -p --mode=777 /simulator/sample_data

sizes[0]='20MB.zip'
links[0]='http://ipv4.download.thinkbroadband.com/20MB.zip'

#sizes[1]='250MBb.png'
#links[1]='https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.A1.png'
#
#sizes[2]='small.csv'
#links[2]='https://www.briandunning.com/sample-data/us-500.zip'
#
#sizes[3]='1GB.zip'
#links[3]='http://ipv4.download.thinkbroadband.com/1GB.zip'
#
#sizes[4]='500MB.zip'
#links[4]='http://ipv4.download.thinkbroadband.com/512MB.zip'
#
#sizes[5]='200MB.zip'
#links[5]='http://ipv4.download.thinkbroadband.com/200MB.zip'
#
#sizes[6]='100MB.zip'
#links[6]='http://ipv4.download.thinkbroadband.com/100MB.zip'
#
#sizes[7]='250MBa.png'
#links[7]='https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.D2.png'

i=0
for link in "${links[@]}"; do
    sudo wget -O '/simulator/sample_data/'${sizes[${i}]} ${link}
    (( i++ ))
done

sudo python3 -m venv /simulator/venv && source /simulator/venv/bin/activate
pip install boto3
deactivate
python