#!/bin/bash

docker run -d --name postdatadb -e POSTGRES_PASSWORD=admin123 -e POSTGRES_USER=postgres -e POSTGRES_DB=registration postgres


docker run -d --name regapp -p 26000:25000 --link postdatadb:postdatadb reg_port 

