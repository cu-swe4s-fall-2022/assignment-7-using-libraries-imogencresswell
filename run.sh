#!/bin/bash


set -u 
set -o pipefail 

python3 plotter.py
pycodestyle data_processor.py
pycodestyle plotter.py
python3 -m unittest test_data_processor.py
bash test_plotter.sh
