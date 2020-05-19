# Installation Instruction faircoin on Docker environment

### Use cases of faircoind@Docker?

Docker makes it quite easy to install and run a full node on different operation systems doesn't matter if Windows or MacOS.

Everybody can build the faircoin deamon from source without to change the local system. ( except of the installation of Docker )

### Preparation

#### Install Docker
* [Windows](https://docs.docker.com/docker-for-windows/)
* [Mac](https://docs.docker.com/docker-for-mac/)
* [centOS](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
* [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/)
* [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


### Installation

#### Build Docker image

If you want to run a full node to support the network then select **build without wallet**

If you want to run a cvn then select **build without wallet and with cvn**

If you want to run a wallet then select **build with wallet**


~~~
cd ~
git clone https://github.com/fairchainsx/faircoin-2-installation

### build without wallet ( full node only ) ###################################################################
sudo docker build --no-cache -t faircoin-v92001-image ~/faircoin-2-installation/docker/

### build without wallet and with cvn #########################################################################
sudo docker build --no-cache --build-arg rule=cvn -t faircoin-v92001-image ~/faircoin-2-installation/docker/

### build with wallet/qt ######################################################################################
sudo docker build --no-cache --build-arg rule=wallet -t faircoin-v92001-image ~/faircoin-2-installation/docker/
~~~

#### Run Docker container ( without wallet )
~~~
sudo docker run -it -d --network="host" -p 8332:8332 --name faircoin-v92001-container faircoin-v92001-image
~~~

#### Create Aliases
add this lines to ~/.bashrc
~~~
alias faircoind="sudo docker exec -it faircoin-v92001-container /opt/faircoin-2/src/faircoind"
alias faircoin-cli="sudo docker exec -it faircoin-v92001-container /opt/faircoin-2/src/faircoin-cli"
alias faircoin.start="sudo docker container start faircoin-v92001-container"
alias faircoin.stop="faircoin-cli stop && sleep 10 && sudo docker container stop faircoin-v92001-container"
alias faircoin.running="sudo docker inspect -f '{{.State.Running}}' faircoin-v92001-container"
~~~
reload configurations
~~~
source ~/.bashrc
~~~

### Usage

#### Start container and faircoin deamon
~~~
faircoin.start
faircoind -daemon
~~~

#### Stop container and faircoin deamon ( f.e. before shutdown )
~~~
faircoin.stop
~~~

#### Get commandline access
~~~
sudo docker attach faircoin-v92001-container
~~~

#### ***IMPORTANT NOTICE***

If you want reboot the system or stop the container dont forget to stop the deamon before to be sure that all downloaded blockchain data will saved in the container!
~~~
faircoin.stop
~~~


#### Use faircoin

##### Commandline API calls
~~~
faircoin-cli help
~~~

##### cURL JSON-RPC calls
~~~
curl --data-binary '{"jsonrpc": "2.0", "id":"curltest", "method": "getinfo", "params": [] }' -H 'content-type: text/plain;' http://faircoin:mypassword@localhost:8332/
~~~

#### Use faircoin by jsonrpc
see the examples ./examples/faircoin_jsonrpc.py
