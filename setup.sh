#!/usr/bin/env bash

echo "vanilla env"
echo
python_bin=/usr/local/anaconda3/envs/vanilla/bin/python
pip_bin=/usr/local/anaconda3/envs/vanilla/bin/pip
${pip_bin} uninstall hopla -y
${pip_bin} install .
${python_bin} setup.py config --config-dir /Users/oliviersteck/Documents/sources/python/hopla_root/hopla/resources/config
echo "---------------------------------------------------------------------------------------------------------------------------------------"

echo

echo "hopla env"
echo
python_bin=/usr/local/anaconda3/envs/hopla/bin/python
pip_bin=/usr/local/anaconda3/envs/hopla/bin/pip
${pip_bin}=/usr/local/anaconda3/envs/vanilla/bin/pip
${pip_bin} uninstall hopla -y
${pip_bin} install .
${python_bin}  setup.py config --config-dir /Users/oliviersteck/Documents/sources/python/hopla_root/hopla/resources/config
${python_bin}  setup.py install --force; python setup.py test
echo "---------------------------------------------------------------------------------------------------------------------------------------"