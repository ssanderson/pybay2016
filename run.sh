#!/bin/bash

venv_name="pybay2016"

if [[ -z "$(type -t workon)" ]];
then
    echo "No function named 'workon' found. Did you execute ./run.sh instead of 'source'-ing?"
    echo "See https://virtualenvwrapper.readthedocs.org/en/latest/install.html"
elif [[ -z "$(lsvirtualenv -b | grep $venv_name)" ]];
then
    echo "No virtualenv named $venv_name found."
else
    workon $venv_name

    # Install module and dependencies editably.
    pip install -e . ./pyxl3
    pip install --pre RISE==4.0.0b1

    jupyter nbextension install rise --py --sys-prefix
    jupyter nbextension enable rise --py --sys-prefix
    jupyter notebook notebooks/Main.ipynb
fi
