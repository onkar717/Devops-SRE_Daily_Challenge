# Day 14 Challenge: Orchestrating Yelb with Docker Compose

Hello EveryOne,

Welcome back to the DevOps SRE Daily Challenge! 🎉

Over the past few days, we’ve explored Docker fundamentals, Dockerfiles, networking, and volumes. 
Today, we’ll take it further by introducing [Docker Compose](https://docs.docker.com/compose/), a tool for easily defining and managing multi-container applications.

By the end of this challenge, you’ll understand how to orchestrate the Yelb application using a docker-compose.yml file, enabling simplified deployment and management of services.



## What is Docker Compose?
Docker Compose is a tool for defining and running multi-container applications. With a single YAML file, you can specify all the required services, networks, and volumes, streamlining deployment and configuration.



## Why Use Docker Compose?
- Simplicity: Replace long Docker commands with a clean YAML configuration.
- Multi-Container Management: Start, stop, and scale all services with a single command.
- Portability: Share the Compose file for consistent deployments across environments.

## Challenge Steps
1. Install Docker Compose:
  - Ensure Docker Compose is installed on your system.
  - Verify installation: ``` docker compose version```
2. Write a docker-compose.yml File
  - Create a docker-compose.yml file to define all Yelb services:
    - Redis: Cache layer.
    - PostgreSQL: Persistent data storage.
    - Appserver: Application logic.
    - UI: User interface.
  - Refer to Yelb project [docker-compose file](https://github.com/mreferre/yelb/blob/master/deployments/localtest/docker-compose.yaml)
3. Deploy the Application
  - Start all services with a single command: ``` docker-compose up -d```
4. Verify the Deployment
  - Check the status of all containers: ``` docker compose ps```
  - Open your browser and visit http://localhost:8080 to interact with the Yelb UI.
5. Stop and Clean Up
  - Bring down all services and remove containers, networks, and volumes: ``` docker compose down --volumes```


