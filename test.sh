#!/bin/sh
cd data
source ../.venv/bin/activate
ls
make validate 
make exec-tests