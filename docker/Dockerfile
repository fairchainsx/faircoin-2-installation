FROM ubuntu:18.04@sha256:5f4bdc3467537cbbe563e80db2c3ec95d548a9145d64453b06939c4592d67b6d

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8
ARG rule="daemon"
# rule = daemon => build without wallet/qt
# rule = wallet => build with wallet/qt
# rule = cvn    => build without wallet/qt with cvn

###########################################################################################
### install base libraries and dependencies for faircoin daemon
RUN apt-get update -q && \
    apt-get install -qy \
        git=1:2.17.1-1ubuntu0.5 \
        make=4.1-9.1ubuntu1 \
        autotools-dev=20180224.1 \
        autoconf=2.69-11 \
        libtool=2.4.6-2 \
        libssl-dev=1.1.1-1ubuntu2.1~18.04.5 \
        libboost-all-dev=1.65.1.0ubuntu1 \
        libevent-dev=2.1.8-stable-4build1 \
        libdb++-dev=1:5.3.21~exp1ubuntu2 \
        libdb-dev=1:5.3.21~exp1ubuntu2

###########################################################################################
### install additional libraries and dependencies for wallet and qt support
RUN if [ "$rule" = "wallet" ]; \
    then apt-get update -q && \
      apt-get install -qy \
        miniupnpc=1.9.20140610-4ubuntu2 \
        libqrencode-dev=3.4.4-1build1 \
        libzmq3-dev=4.2.5-1ubuntu0.2 \
        qttools5-dev-tools=5.9.5-0ubuntu1 \
        libprotobuf-dev=3.0.0-9.1ubuntu1 \
        protobuf-compiler=3.0.0-9.1ubuntu1; \
    fi

###########################################################################################
### install nano commandline editor [optional] ( to edit faircoin.conf later if necessary )
RUN apt-get install -qy nano=2.9.3-2

###########################################################################################
### system cleanup
RUN rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

###########################################################################################
### download and build faircoin daemon and cli
RUN cd /opt && \
    git clone https://github.com/fairchainsx/faircoin-2.git

RUN cd /opt/faircoin-2 && ./autogen.sh

RUN if [ "$rule" = "daemon" ]; then cd /opt/faircoin-2 && ./configure --disable-tests --disable-bench --with-incompatible-bdb --disable-wallet; fi
RUN if [ "$rule" = "wallet" ]; then cd /opt/faircoin-2 && ./configure --disable-tests --disable-bench --with-incompatible-bdb; fi
RUN if [ "$rule" = "cvn" ]; then cd /opt/faircoin-2 && ./configure --disable-tests --disable-bench --with-incompatible-bdb --disable-wallet --with-cvn; fi

RUN cd /opt/faircoin-2 && make

###########################################################################################
### create faircoin.conf ( change it if necessary and set another port or password )
RUN mkdir /root/.faircoin2 && \
    echo -e "rpcconnect=127.0.0.1\nrpcport=8332\nrpcuser=faircoin\nrpcpassword=mypassword\ntxindex=1" > /root/.faircoin2/faircoin.conf

###########################################################################################
### initialize blockchain with txindex=1
RUN cd /opt/faircoin-2/src && \
    ./faircoind -daemon -reindex && \
    sleep 60 && \
    ./faircoin-cli stop && \
    sleep 10
