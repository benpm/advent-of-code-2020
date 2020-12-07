#!/bin/bash
mkdir original_solutions/day_$1
cd original_solutions/day_$1
cp ../../boilerplate.py ./day_$1A.py
cp ../../boilerplate.py ./day_$1B.py
touch input_$1.txt
touch test_input.txt