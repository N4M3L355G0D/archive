#! /bin/bash
config=wps-office.cfg

bash wps_downloads.sh

pack32=`python3 linkExtract.py | grep "x86.tar.xz"`
pack64=`python3 linkExtract.py | grep "x86_64.tar.xz"`

echo "source32=$pack32" > "$config"
echo "source64=$pack64" >> "$config"

rm ./download.html
