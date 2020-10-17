# Dockerized IL2 Stats server
This repository contains code to run IL2 Stats version 1.2.44 in a docker-compose environment.

The original package is provided here by: **=FB=Vaal**
> https://forum.il2sturmovik.com/topic/19083-il2-stats-statistics-system-for-a-dedicated-server-il2-battle-of-stalingrad/

It comes with 3 services:
* IL2 Stats: The main website you want to access to
* PostgreSql: The database that will store the statistics and the users accounts 
* PGAdmin: A web interface to access the database and see/edit data. 

## Configurations

Before starting, some configurations are needed:
* `docker-compose.yml`:

  * il2stats-web section
    * ADMIN_EMAIL: the email to login to the admin panel of the il2stats website
    * ADMIN_PASSWORD: the password for the same thing
    * volumes: this settings links the IL2 game folder to a internal location in the container. Change the `/mnt/il2/` part (just before the column) to the path of your local IL2 installation

  * db section
    * POSTGRES_PASSWORD: password to access the postgres DB. This MUST be also configured in the `conf.ini` file of il2stats
    * POSTGRES_USER: same as before, but for the username
    * volumes: this links the content of the database inside the container to a folder in your current (real) machine. You can for example create a folder in your `/User/../Documents/il2stats_db`. As in the other case, just change the first part of the string, before the column symbol `~/il2stats_db`
* `il2_stats/src/conf.ini`:
  * Search for the `[database]` section and change ONLY the USER and PASSWORD values. The values MUST be the same as those already defined in the docker-compose.yml in the `db` section for POSTGRES_USER and POSTGRES_PASSWORD

## Startup
If you stil didn't do it, go to the [Configurations](#Configurations) chapter before trying to run the system.


To run everything, just run the docker compose file: 
```
docker-compose up -d
```

If you want to see what's going on in one of the containers, run: 
```
docker-compose logs -f il2stats-web
```
Instead of `il2stats-web` you can also use `postgres` or `pgadmin` to view the related services logs.

If you need to debug something inside the component, run: 
```
docker exec -it il2stats-web bash
```
Instead of `il2stats-web` you can also use `postgres` or `pgadmin` to view the related services logs.

In case things don't work anymore for some reason, you could try resetting everything:
```
docker-compose rm -f
```
After that `run docker-compose up -d` and cross your fingers 🤞

## Note about Postgres container
Once started the first time, username and password cannot be changed by just changing the content of the docker-compose.yml file. This is a limitation of the postgres container.