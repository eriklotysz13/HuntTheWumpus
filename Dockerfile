# use python image
FROM python:3.10-slim

# set the working directory in the container
WORKDIR /app

# copy all files into the container
COPY . .

# command to run the game
CMD ["python", "main.py"]
