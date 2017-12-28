#! /bin/bash

installer_dir="/$2/"
bin="/opt/bin/"
ln -s "$installer_dir$1" "$bin"
