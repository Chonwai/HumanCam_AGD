#!/bin/bash
echo python3 --version
echo ${BASH_ARGV[*]}

python age_and_gender_detection_live.py ${BASH_ARGV[*]}