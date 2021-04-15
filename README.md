The part of the project is created to have the OSS Assignment 4. This Part has been done by Sankatmochan and Saravana

## Python Dockerfile

This repository contains a simple docker file for creating docker image for python execution.

 **Dockerfile** of [Python](https://www.python.org/) for [Docker](https://www.docker.com/)'s [automated build](https://registry.hub.docker.com/u/dockerfile/python/) published to the public [Docker Hub Registry](https://registry.hub.docker.com/).

### Base Docker Image

* [dockerfile/ubuntu](http://dockerfile.github.io/#/ubuntu)

### Installation

1. Install [Docker](https://www.docker.com/).

2. Download [automated build](https://registry.hub.docker.com/u/dockerfile/python/) from public [Docker Hub Registry](https://registry.hub.docker.com/): `docker pull dockerfile/python`

   (alternatively, you can build an image from Dockerfile: `docker build -t="dockerfile/python" github.com/dockerfile/python`)


### Usage

    docker run -it --rm dockerfile/python

#### Run `python`

    docker run -it --rm dockerfile/python python
    
#### Addedd files for Basic Calculation

    BasicCalculator.py: Does basic calculation upon user inputs.

    Select operation.
    1.Add
    2.Subtract  
    3.Multiply
    4.Divide

    Enter choice(1/2/3/4): 1
    Enter first number: 5
    Enter second number: 4
    5.0 + 4.0 = 9.0


#### Addedd files to Add and substract 2 numbers

    Addition.py: Add two Number
    Substraction.py: Subctract two numbers

#### Addedd files to Multiply and Division 2 numbers

    Multiplication.py: Multiply two Numbers
    Division.py: Divide two numbers

#### Addedd files for square root function

    squareroot.py: Performs square root function.
    
#### upgraded Multiply and Division files for better performance

 Multiplication.py: Multiply numbers in a list
    Division.py: Divide two numbers using floor

