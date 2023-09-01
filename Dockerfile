# syntax=docker/dockerfile:1

# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .
