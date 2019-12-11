# Installation Instruction faircoin on Ubuntu18.04

### Installation

~~~
sudo apt-get update -q
sudo apt-get install -qy \
    git \
    make \
    autotools-dev \
    autoconf \
    libtool \
    libssl-dev \
    libboost-all-dev\
    libevent-dev \
    libdb++-dev \
    libdb-dev \
    nano

cd ~ && \
git clone https://github.com/fairchainsx/faircoin-2.git

cd ~/faircoin-2
./autogen.sh
./configure --disable-tests --disable-bench --disable-wallet
make

mkdir ~/.faircoin2
echo -e "rpcconnect=127.0.0.1\nrpcport=8332\nrpcuser=faircoin\nrpcpassword=mypassword\ntxindex=1" > ~/.faircoin2/faircoin.conf

cd ~/faircoin-2/src
./faircoind -daemon -reindex && \
sleep 60 && \
./faircoin-cli stop && \
sleep 10
~~~
