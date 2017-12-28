#! /bin/bash

installer_dir="/opt/software/$2/"
bin="/opt/bin/"
ln -sf "$installer_dir$1" "$bin"
