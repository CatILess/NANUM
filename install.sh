ROOTDIR=${PWD}
MODULES=${ROOTDIR}/modules

#portspoof
echo "Install portspoof....."
sudo apt-get install g++ make

cd $MODULES/portspoof
./configure
make
sudo make install
sudo cp ./system_files/init.d/portspoof.sh /etc/init.d/portspoof
sudo chmod +x /etc/init.d/portspoof

#cowrie
echo "Install cowrie......"
sudo apt-get install git python-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind
cd $MODULES/cowrie
virtualenv --python=python3 cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install --upgrade -r requirements.txt
pip install bcrypt


