#!/bin/bash
##################################
# AI with Python Vagrant Machine #
#     by FEARLESS SPIDER         #
##################################
function install {
    echo installing "$1"
    shift
    apt-get -y install "$@" >/dev/null 2>&1
}

function pip_install {
    echo installing "$1"
    shift
    pip3 install "$@" >/dev/null 2>&1
}

echo "updating package information"
apt-get -y update >/dev/null 2>&1

# Theano
install 'pip3' python3-pip build-essential libssl-dev libffi-dev
install 'theano dependencies' python3-numpy python3-scipy python3-dev python3-nose g++ git libatlas3gf-base libatlas-dev
pip_install 'theano' theano

# Keras
pip_install 'keras' keras

# Tensorflow
pip_install 'tensorflow' tensorflow

# Miscellaneous
pip_install 'required Python libraries' pyyaml cython
install 'hdf5' libhdf5-7 libhdf5-dev
pip_install 'h5py' h5py
pip_install 'ipython' ipython
pip_install 'jupyter' jupyter
pip_install 'scikit-learn' scikit-learn
pip_install 'neurolab' neurolab
pip_install 'matplotlib' matplotlib

echo 'All set!'