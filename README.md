# Ultimate frisbee or not
A convolutional neural network that classifies images of sports as ultimate frisbee or not.

## Setup
This project uses the python package manager Conda with an environment.yml file. To import the environment run
```
conda env create -f environment.yml
```
If the environment was updated, run
```
conda env export > environment.yml
```
to update those changes in the environment.yml file.

## Build
To build to docker image for this project run:

```
docker build ./ -t fris
```

## Run
for development:
```
python src/wsgi.py
```

for production:
```
docker run --name fris -p 80:5000 --rm fris:latest
```