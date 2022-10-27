#!/bin/bash


set -u 
set -o pipefail 

pycodestyle data_processor.py
pycodestyle test_utils.py
pycodestyle plotter.py
python3 -m unittest test_data_processor.py
bash test_plotter.sh
