#!/bin/bash
#wrapper script for invoking docker image
#command tool

#run command, if interupt flaged, remove the docker image to end gracefully
trap 'sudo docker stop $(sudo docker ps -a -q --filter ancestor=zdalihach/gmpract:alpha --format="{{.ID}}")' INT
sudo docker run --rm -t zdalihach/gmpract:alpha "$@"
