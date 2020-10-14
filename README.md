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
* Each file in the "secrets" folder, represent a secret that only you should know. Those are variable such ase email and password to access the db, pgadmin or the il2stats admin panel. Change them as you prefer. Please always have letters, numbers and special characters in the passwords.
* The il2stats_config.ini file is the main configuration for the Il2 Stats server. It is **VERY IMPORTANT** that the database.user and database.password fields here are the same as the one configured in the postgres_user.txt and postgres_password.txt secret files. Any inconsistency, would break the connection between Il2 Stats and the database.
* Open the docker-compose.yml and search for the `game_folder` volume, at the bottom of the file. There will be 2 instances of it, only the one at the bottom has a big PATH pointing at the IL2 game folder. Change the path so that it corresponds to the one on your machine.

## Startup
If you stil didn't do it, go to the [Configurations](#Configurations) chapter before trying to run the system.


To run everything, just run the docker compose file: 
```
docker-compose up
```

If you want to see what's going on in one of the containers, run: 
```
docker-compose logs il2stats-web
```
Instead of `il2stats-web` you can also use `postgres` or `pgadmin` to view the related services logs.