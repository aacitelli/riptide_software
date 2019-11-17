#!/bin/bash

sudo pip install vcstool 

mkdir  ../riptide_software/
mkdir ../riptide_software/src
cd ..

cp repos/riptide_base.repos .

vcs import < riptide_base.repos riptide_software/src




cd riptide_software
cd src
cd riptide_utilities
cd setup_scripts


cd ..
cd ..
cd ..
cd ..
cd repos



