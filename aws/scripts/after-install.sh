#!/bin/bash
set -xe

# TODO: in production mode
# Copy whl file from S3 bucket to flask webapp folder
# Ensure the ownership permissions are correct.
/root/.local/bin/virtualenv -p python3 ./venv
chmod -R a+rwx venv
source ./venv/bin/activate
pip3 install -r requirement.txt