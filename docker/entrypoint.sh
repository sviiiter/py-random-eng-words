#!/bin/bash

cd /app

pip install -r /app/requirements.loc

python3 parser.py

python3 polling.py
