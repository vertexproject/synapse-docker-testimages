#!/usr/bin/env bash
git clone https://github.com/vertexproject/synapse.git  ./synapse
cd ./synapse
nosetests --verbosity=3
