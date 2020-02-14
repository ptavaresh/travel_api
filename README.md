# travel_api
Personal project: I want to remember myself in a long term future all the places that i have been, I have explored just few places but I hope they increse in the future :)

## Create docker image
docker build -t travel_api -f Dockerfile .

## Create docker container
docker run -it -d -p 8000:8000 travel_api
