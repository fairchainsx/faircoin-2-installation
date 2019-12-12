# Installation Instruction faircoin on Ubuntu18.04

### Installation

#### base dependencies / libraries for faircoin daemon ( mandatory )
~~~
###############################################################################
# install base dependencies / libraries
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
~~~

#### additional libraries and dependencies for wallet and qt support ( optional )
~~~
###########################################################################################
# install additional libraries and dependencies for wallet and qt support
sudo apt-get update -q && \
sudo apt-get install -qy \
    miniupnpc \
    libqrencode-dev \
    libzmq3-dev \
    qttools5-dev-tools \
    libprotobuf-dev \
    protobuf-compiler
~~~

#### Build binaries
~~~
###############################################################################
# download faircoin sources / git
cd ~
git clone https://github.com/fairchainsx/faircoin-2.git

###############################################################################
# make all binaries ( faircoind, faircoin-cli, faircoin-tx )
cd ~/faircoin-2
./autogen.sh

# configure without wallet ###################################
./configure --disable-tests --disable-bench --disable-wallet

# configure with wallet/qt ###################################
./configure --disable-tests --disable-bench --with-incompatible-bdb

make
~~~

#### Create faircoin.conf and initialize blockchain for jsonRPC support (optional)
~~~
###############################################################################
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

all binaries are in `~/faircoin-2/src`

#### Create Aliases (optional)
add this lines to ~/.bashrc
~~~
alias faircoind="~/faircoin-2/src/faircoind"
alias faircoin-cli="~/faircoin-2/src/faircoin-cli"
~~~
reload configurations
~~~
source ~/.bashrc
~~~
Now you can run `faircoind`, `faircoin-cli` and `faircoin-qt` on commandline.
