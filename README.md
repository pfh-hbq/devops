[![debops-ci Actions Status](https://github.com/pfh-hbq/devops/workflows/devops-ci/badge.svg)](https://github.com/pfh-hbq/devops/actions) 


# DevOps Lab 01
๐จ๐ปโ๐ป Zarubin Iurii, BS18-SE-01

๐ Innopolis University


## ๐ฟ Simple Python web application, that shows current time in Moscow ๐

### ๐  Run natively

`install requirements.txt`

### ๐ณ Run using Docker

Docker image is available [here](https://hub.docker.com/r/pfhhbq/devops_lab01)

`docker build -t devops_lab01 .`

`docker run --rm -p 5000:5000 devops_lab01`

### ๐งช Run tests

`pytest`

## ๐ฑ Bonus task for lab01 - Free iPhone single-page application

go to the app_vuejs folder and see requirements there

Docker image is available [here](https://hub.docker.com/r/pfhhbq/devops_lab02_bonus)

`docker build -t devops_lab02_bonus .`

`docker run -it -p 8080:8080 --rm devops_lab02_bonus`

go to http://127.0.0.1:8080

