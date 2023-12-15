
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

(Provide instructions on how to install or set up your package, e.g., cloning a repository, installing through pip, etc.)

Example:
```bash
pip install your-package-name
```

## Usage

To use this package, you need a YAML file with configurations for the endpoints you wish to monitor.

## Testing

The package includes comprehensive unit tests to ensure the functionality's reliability and correctness.

### Running Tests

To run the tests, use the following command:

```bash
python -m unittest test_endpoint_monitor.py
```
