#! /bin/sh
pip3.6 uninstall -y kdfconn
python3.6 setup.py sdist bdist_wheel
cd ./dist
pip3 install kdfconn-0.0.1-py3-none-any.whl