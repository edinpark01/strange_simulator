#!/usr/bin/env bash

ec2_region=$1

sudo yum install -y wget python3

mkdir -p --mode=777 /simulator/sample_data

sizes[0]='250MBa.png'
links[0]='https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.D2.png'

sizes[1]='250MBb.png'
links[1]='https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.A1.png'

sizes[2]='small.csv'
links[2]='https://www.briandunning.com/sample-data/us-500.zip'

sizes[3]='1GB.zip'
links[3]='http://ipv4.download.thinkbroadband.com/1GB.zip'

sizes[4]='500MB.zip'
links[4]='http://ipv4.download.thinkbroadband.com/512MB.zip'

sizes[5]='200MB.zip'
links[5]='http://ipv4.download.thinkbroadband.com/200MB.zip'

sizes[6]='100MB.zip'
links[6]='http://ipv4.download.thinkbroadband.com/100MB.zip'

sizes[7]='20MB.zip'
links[7]='http://ipv4.download.thinkbroadband.com/20MB.zip'


i=0
for link in "${links[@]}"; do
    sudo wget -O '/simulator/sample_data/'${sizes[${i}]} ${link}
    (( i++ ))
done

sudo python3 -m venv /simulator/venv && source /simulator/venv/bin/activate
pip install boto3
python /simulator/simulator.py ${ec2_region}