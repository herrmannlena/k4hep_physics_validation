git clone https://github.com/key4hep/k4-project-template
cp ci-scripts/gaudi.py ci-scripts/k4-project-template/k4ProjectTemplate/options/
cd k4-project-template
#source /cvmfs/sw-nightlies.hsf.org/key4hep/setup.sh
k4_local_repo
mkdir build install
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install
make -j 4 install
cd ../../../
