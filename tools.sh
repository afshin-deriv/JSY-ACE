apt-get update -y
apt-get install -y nmap tcpdump socat netcat curl gdb automake strace ltrace

#XOCopy: http://reverse.lostrealm.com/tools/xocopy.html
wget http://reverse.lostrealm.com/tools/xocopy.c
make xocopy

#pwndbg: https://github.com/pwndbg/pwndbg
cd /tmp
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh

#v0lt: https://github.com/P1kachu/v0lt
cd /tmp
git clone https://github.com/P1kachu/v0lt.git
cd v0lt
python3 setup.py install

#pwntools: https://github.com/Gallopsled/pwntools
apt-get install python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools

#checksec
cd /opt
git clone --depth 1 https://github.com/slimm609/checksec.sh
cd checksec.sh/
ln -s /opt/checksec.sh/checksec /bin/checksec

#valgrind
cd /opt
INST_DIR=$PWD
curl ftp://sourceware.org/pub/valgrind/valgrind-3.13.0.tar.bz2 | tar xj
cd valgrind-3.13.0
./autogen.sh
./configure --prefix=$INST_DIR
make -j $(nproc)
make install
ln -s /opt/bin/valgrind  /bin/valgrind