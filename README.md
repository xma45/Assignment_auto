# Assignment_auto
Assignment from interview process


# This project is runnable with environment variables in the docker container
# To enable the logger for response, change the dockerfile ENV vairable from "ABC" to "DEV"
# The ENV variable cannot be None

# To build the docker container
docker build --tag assignment_auto .

# To run this project
docker run assignment_auto


