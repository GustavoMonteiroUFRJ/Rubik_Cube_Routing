#!/bin/bash

# isntala os pacotes necessarios para doar o DeepCubeA na instancia g4dn.xlarge da AWS

sudo apt update
sudo apt install python2.7 -y
sudo apt install python-pip -y

sudo pip install setuptoolsls

sudo pip install "tensorflow-gpu==1.8.0"
sudo pip install "tensorflow==1.8.0"
sudo pip install sonnet
