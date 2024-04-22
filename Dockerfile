FROM python:3.11.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /octopus_school_test

# Set the working directory to /music_service
WORKDIR /octopus_school_test

# Copy the current directory contents into the container at /music_service
ADD . /octopus_school_test/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
