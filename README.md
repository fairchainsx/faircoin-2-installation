# FairCoin Installations
( by docker-compose / without qt wallet )
### Requirements

* Docker Engine
* Docker Compose

https://docs.docker.com/compose/install/


## Run a Full Node

### Usage

At first download the faircoin installation repository.

~~~
git clone https://github.com/fairchainsx/faircoin-2-installation.git
cd docker-compose
~~~

#### Build

Before you can start the container you need to (re)build it by ...

~~~
docker-compose build faircoin
~~~

Notice that when you (re)build the container then all blockchain data will need to be downloaded again!

#### Start

~~~
docker-compose start faircoin
~~~

#### Stop

Normally the container will started automatically while the systems boot. `( docker-compose.xml -> restart: always )` and stopped before shutdown.
But if you want stop the container while your system is running then you can do this by ...

~~~
docker-compose stop faircoin
~~~

and the container will stopped. Notice that the container will started again by the next boot.

Don't use `docker-compose down` because in this case the container will not only stopped but also removed and all blockchain data needs to be downloaded again.

#### Access to container

Normally it is not necessary to get access to the container. But if you need access to the container because you want change the configuration or run the faircoin-cli then you can do this by ...

~~~
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
# list running containers
docker ps

# list all containers
docker ps --all
~~~


# Run a ElectrumX server
