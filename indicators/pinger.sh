#! /usr/bin/bash

ping -c 1 techzone.org | ./pingfilter.awk
