
# Endpoint Monitoring Package

## Exercise Overview

Implement a program to check the health of a HTTP endpoints every 15 seconds until user manually exits the program. The input to the program should be path to yaml file containing endpoints. 

## Description

This package provides a solution for monitoring the health and availability of HTTP endpoints. It is designed following the SOLID principles of object-oriented programming, ensuring the system is both extendable and maintainable.

## Features

- **Configurable Endpoint Monitoring**: Monitor a variety of endpoints as defined in a YAML configuration file.
- **Health Checking**: Perform health checks on endpoints using HTTP requests.
- **Availability Logging**: Keep track of endpoint availability and log statistics.
- **SOLID Principles**: Adherence to SOLID principles, particularly the Dependency Inversion Principle, for easy extension and maintenance.

## Installation
Clone the this repository and change directory to the repository. 

Feel free to download the zip from the github if `git clone` is not working for some reasons.

```bash
git clone https://github.com/shivams1208/fetch_rewards_SRE_take_home.git

cd fetch_rewards_SRE_take_home
```

## Usage
To use this package, you need a YAML file with configurations for the endpoints you wish to monitor. 
I have created `endpoints.yaml` file in `src/` directory which contains Sample Input file from assignment doc for convenience but you can provide the path to any yaml file as input to the program.

I have provided two ways to use this package:

### 1. By installing dependencies and python
To avoid any issues related to different versions of dependencies I recommend:
1. Install Python 3.9.7:

   1. Visit the [Python Releases page](https://www.python.org/downloads/release/python-397/) and download the file as per relevant OS.
   2. Once the installer is downloaded, open it and follow the installation instructions. This will typically involve clicking through a setup wizard.
   3. After installation, open a terminal and run python3 --version or python3.9 --version to check if Python 3.9.7 is installed correctly.

2. Install pyyaml-6.0.1:

Make sure you have pip installed. You can check this by running `pip --version` or `pip3 --version` in the terminal. Use `pip` or pip3` depending upon whichever is available in your system.

   1. `pip install pyyaml==6.0.1`
   2. If you have both Python 2 and Python 3 installed, you might need to use pip3:
      1. `pip3 install pyyaml==6.0.1`
3. Install requests-2.31.0:

Make sure you have pip installed. You can check this by running `pip --version` or `pip3 --version` in the terminal. Use `pip` or pip3` depending upon whichever is available in your system.

   1. `pip install requests==2.31.0`
   2. If you have both Python 2 and Python 3 installed, you might need to use pip3:
      1. `pip3 install requests==2.31.0`

Now that we have all the required dependencies, let's get the program running:
1. `python3 src/endpoint_monitor.py` or `python src/endpoint_monitor.py` depending upon available python version in your system.
2. Now the script if ask for path to the `yaml` file, **although you can provide the path to the sample file which I have included in `src` folder but it should work for any arbitrary path to yaml file.**
   * *While providing the input you do not need to provide the path as string.*
   * Path to sample yaml: `src/endpoints.yaml`


*Now if you don't want to go over the hustle of installing above dependencies and just want to see the program working for sample yaml file then you can use Docker.*
### 2. Using Docker:
First make sure you have docker installed in your system and if not you can get the docker from [here](https://docs.docker.com/get-docker/).

This method is built from the mindset that reviever doesn't necessarily have same system using which I have created the solution and doesn't have to go through the hassle of installing dependencies for verifying the solution. 

a. Build the docker:

`docker build -t endpoint_monitor .`

b. Run the docker:

`docker run -it endpoint_monitor python3 src/endpoint_monitor.py` or `docker run -it endpoint_monitor python src/endpoint_monitor.py` depending upon python version in your system

c. Providing Input:

*While providing the input you do not need to provide the path as string.*

Now since you are running a Docker container, it has its own isolated file system separate from your host machine. This means providing any arbitrary path on local would not work since it cannot be accessed from the docker container. **Although, this program can accept any arbitrary yaml file path but when using it with docker only yaml input present in src can be utilised since that's the way docker has built the package.**
   * `src/endpoints.yaml`
  

## Testing

The package includes comprehensive unit tests to ensure the functionality's reliability and correctness. The unit tests are included in src/tests directory and segregated into different files for each class.

### Running Tests

To run the tests, use the following command depending upon whether you use dependencies or docker for usage:

1. By installing dependencies and python:
   1. `cd src`
   2. `python3 -m unittest discover -s tests` or `python -m unittest discover -s tests` depending upon python version in your OS
2. Using docker: 
   1. `docker run -it endpoint_monitor /bin/bash run_tests.sh`
