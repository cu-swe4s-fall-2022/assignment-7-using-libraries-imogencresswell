#!/bin/bash
test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_for_success \
    python3 ./plotter.py
assert_in_stdout 'iris_boxplot.png'
assert_in_stdout 'petal_width_v_length_scatter.png'
assert_in_stdout 'multi_panel_figure.png'
assert_exit_code 0
