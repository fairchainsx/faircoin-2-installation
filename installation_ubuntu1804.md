# Installation Instruction faircoin on Ubuntu18.04

### Installation

~~~
#######################################
# preparation | install dependencies / libraries
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
    libdb-dev

#######################################
# download faircoin sources / git
cd ~
git clone https://github.com/fairchainsx/faircoin-2.git

#######################################
# make all binaries ( faircoind, faircoin-cli, faircoin-tx )
cd ~/faircoin-2
./autogen.sh
./configure --disable-tests --disable-bench --disable-wallet
make

#######################################
# create rpc configurations [optional]
mkdir ~/.faircoin2
echo -e "rpcconnect=127.0.0.1\nrpcport=8332\nrpcuser=faircoin\nrpcpassword=mypassword\ntxindex=1" > ~/.faircoin2/faircoin.conf

########################################
# start blockchain with index [optional]
cd ~/faircoin-2/src
./faircoind -daemon -reindex && \
sleep 60 && \
./faircoin-cli stop && \
sleep 10
~~~

`faircoind` and `faircoin-cli` in `~/faircoin-2/src`


#### Create Aliases
add this lines to ~/.bashrc
~~~
alias faircoind="~/faircoin-2/src/faircoind"
alias faircoin-cli="~/faircoin-2/src/faircoin-cli"
~~~
reload configurations
~~~
source ~/.bashrc
~~~
Now you can run `faircoind` and `faircoin-cli` on commandline.
