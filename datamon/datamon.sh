#! /bin/bash
ip -h -s addr show dev wlp7s0 | tail -n4 | head -n 2 
