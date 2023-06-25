#!/bin/bash

#! /bin/sh

cmd=$1
db_username=$2
db_password=$3

sudo systemctl status docker || systemctl start docker #todo

docker container inspect jrvs-psql
container_status=$?

case $cmd in 
  create)

  if [ $container_status -eq 0 ]; then
		echo 'Container already exists'
		exit 1	
	fi

  if [ $# -ne 3 ]; then
    echo 'Create requires username and password'
    exit 1
  fi
 
	docker volume create pgdata#todo
	docker run --name $db_username -e POSTGRES_PASSWORD=$db_password -d -v pgdata:/var/lib/postgresql/data -p 5432:5432 postgres:9.6-alpine #todo
	exit $?
	;;

  start|stop) 
  if [ $container_status -eq 0 ]; then #todo
  #todo

	docker container $cmd jrvs-psql
	echo 'Docker container $cmd'
	docker ps -all
	exit $?
  fi
	;;	
  
  *)
	echo 'Illegal command'
	echo 'Commands: start|stop|create'
	exit 1
	;;
esac 
