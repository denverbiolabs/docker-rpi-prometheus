# docker-rpi-prometheus

A Raspberry Pi / ARMv7 compatible Docker image with Prometheus and Cross-build support

Tested with a Raspberry Pi 3. SSH into the pi then follow the process below.

## Install Docker
```
curl -sSL get.docker.com | sh
```

## Set Docker to auto-start
```
sudo systemctl enable docker
sudo systemctl start docker
```

## Enable Docker client
```
sudo usermod -aG docker pi
```

## Clone repo and cd into it
```
git clone git@github.com:denverbiolabs/lab-iot-prometheus.git
cd lab-iot-prometheus-master/
```

## Build from Dockerfile
```
docker build -t my-docker-image .
```

After the build process you can run it with the following command.

## Run the docker image to launch Prometheus

```
docker run my-docker-image
```

Use the following command if you want to access the docker image *my-docker-image*.

## How to Access a Docker Image (Optional)

```
docker run -d -p 9090:9090 my-docker-image
```

This will return a 65 character long hash. Copy and paste the hash after -it in the following command.

```
docker exec -it <insert hash here> /bin/bash
```

References

* http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/
* https://prometheus.io/docs/introduction/install/
