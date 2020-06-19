# FairCoin Installations
( by docker-compose / without qt wallet )

## Available Services
* `faircoin` - [Faircoin full node](https://github.com/fairchainsx/faircoin-2)
* `fairchains` - [FairChains full node](https://github.com/FairChains/fairchains) **( prepared but not tested! )**
* `electrumx` - [electrumfairchainsx](https://github.com/fairchainsx/electrumfairchainsx) ( available in combination of services FairCoin & FairChains )

## Requirements

* Docker Engine
* Docker Compose

https://docs.docker.com/compose/install/

## Configuration

All configuration files are stored in the subfolder `./.fairchains`

If you run the faircoin services on a local machine then you can use the repositories configuration files.

If you run the services on a webserver then it is very recommend to replace the ssl files ( .crt and .key ) and change the `rpcpassword` in the `faircoin.conf` / `fairchains.conf` !

If you want to run the services for other fairchains then you need to replace the fairchains json files !

If you run `electrumx` in combination with `faircoin` then you need all fairchains files because the electrumx is made for all fairchains. That means that you need to ensure that your config in `faircoin.conf` is the same as in `fairchains.conf` except the `netname`.
The `netname` should not set in the `faircoin.conf` but is necessary and different in the `fairchains.conf`.

~~~
### faircoin full node config ( mandatory for service `faircoin` )
.fairchains/faircoin.conf

### fairchains config ( mandatory for service `fairchains` and `electrumx` )
.fairchains/fairchains.conf
.fairchains/<netname>.json
.fairchains/<netname>.electrumx.json

### ssl files to run electrumx ( mandatory for service `electrumx` )
.fairchains/electrumx.crt
.fairchains/electrumx.csr  # not necessary but created by openssl ;-)
.fairchains/electrumx.key
~~~

### Create SSL certificate

Create SSL certificates by openssl
~~~
openssl genrsa -out electrumx.key 2048
openssl req -new -key electrumx.key -out electrumx.csr
openssl x509 -req -days 1825 -in electrumx.csr -signkey electrumx.key -out electrumx.crt
~~~

### ElectrumX server

If you want to make the server available on your webdomain then you need to adjust the `SERVICES` array in `./.fairchains/*.electrumx.json`

local:
~~~
"SERVICES" : [
    "rpc://127.0.0.1:8002",
    "ssl://127.0.0.1:51812"
]
~~~

remote ( example domain server.faircoin.co ):
~~~
"SERVICES" : [
    "rpc://127.0.0.1:8002",
    "ssl://server.faircoin.co:51812"
]
~~~

more details you can find in the bitcoin electrumx docs: https://electrumx.readthedocs.io/en/latest/environment.html

## Installation and Usage

At first download the faircoin installation repository.

~~~
git clone https://github.com/fairchainsx/faircoin-2-installation.git
cd faircoin-2-installation
~~~

#### Build and Start
You can build and run a service by only one command. If the container isn't built then the docker-compose will do it. If the container already exists then docker-compose starts it.
If dependencies to other services exists then the other services will build/started before.

If in the `docker-compose.yml` is `restart: always` then your services will stopped and restarted while shutdown and boot automatically. ( https://docs.docker.com/compose/compose-file/#restart_policy )

~~~
docker-compose up
~~~

In the case you need to rebuild the container you can append the option `--build`. Notice that all data ( blockchain data ) inside the old container will going lost. Btw. don't run the command `docker-compose down` because the container will stopped and removed.

#### Manual Actions

Sometimes it can be necessary to build the image without to start the container or start/stop the container seperately or run commands inside the container.

Here are some helpful commands ( on example service `faircoin` )...

~~~
### build service `faircoin` (w/o to start container ) ................................................
docker-compose build faircoin

### start service `faircoin` ( ignore dependencies to other services ) ................................
docker-compose start faircoin

### stop service `faircoin` ( ignore dependencies to other services , container will not removed ) ....
docker-compose stop faircoin

### stop all services ( containers will not removed, all data are  safe ) .............................
docker-compose stop

### remove service container ( data will going lost!! ) ...............................................
docker-compose rm faircoin

### run commands inside the container, here are examples ..............................................
docker-compose exec faircoin <your command>
docker-compose exec faircoin nano .faircoin2/faircoin.conf
docker-compose exec faircoin ./faircoin-cli help

~~~

#### Check if your container is running

Show the status of all defined container in the docker-compose.yml in the current path.
~~~
docker-compose ps
~~~

If you are outside the path and want checking the status of your container then you can do this by the docker command.

~~~
### list running containers ..........................................................................
docker ps

### list all containers ..............................................................................
docker ps --all
~~~
