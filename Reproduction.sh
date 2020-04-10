#!/bin/bash

# Esse script simples reproduz a resolução do cubo mágico nos casos de exemplo.

curl https://codeload.github.com/GustavoMonteiroUFRJ/Rubik_Cube_Routing/zip/master --output Rubik_Cube_Routing.zip
unzip Rubik_Cube_Routing.zip 

cd Rubik_Cube_Routing-master/code 
export CUDA_VISIBLE_DEVICES=1
python scripts/solveStartingStates.py --input ../data/data_25_X_Patter.pkl --env cube3 --methods nnet --model_loc savedModels/cube3/1/ --nnet_parallel 100 --depth_penalty 0.2
