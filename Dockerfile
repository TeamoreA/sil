# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /sil_service

# Set the working directory to /sil_service
WORKDIR /sil_service

# Copy the current directory contents into the container at /sil_service
ADD . /sil_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt