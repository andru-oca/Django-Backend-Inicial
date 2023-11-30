#!/usr/bin/env bash
 
count=0
alive="no"
 
while [ "$count" -lt 6 ]; do
    health=$(docker inspect --format "{{.State.Health.Status}}" "$(docker-compose ps -q mysql)")
 
    if [ "$health" == "healthy" ]; then
        alive="yes"
        break
    fi
 
    echo "waiting for mysql: $health"
    sleep 10
    count=$((count+1))
done
 
if [ "$alive" = "yes" ]; then
    exit 0
else
    echo "MySQL did not start up in time"
    exit 1
fi