# Day 11 - Docker Challenge: Getting Your Feet Wet with Docker

Hello EveryOne,

Welcome back to the DevOps SRE Daily Challenge! 🎉

This week, we’re diving deep into Docker, the cornerstone of containerization.
Today’s challenge will set the foundation by helping you install Docker, explore its essential commands, and build your first custom container. By the end of this challenge, you’ll have a strong grip on Docker fundamentals and an understanding of how to run and manage containerized applications.

## What is Docker?
Docker is an open platform that helps developers and DevOps teams build, ship, and run applications in isolated environments called containers. It simplifies software development, deployment, and scalability by packaging applications with all dependencies needed to run consistently across various environments.

## Why Do We Need Docker?
- Consistency: It eliminates the "works on my machine" problem by ensuring the application behaves the same everywhere.
- Portability: Containers can run anywhere—on laptops, servers, cloud, or Kubernetes clusters.
- Efficiency: Lightweight compared to virtual machines, as containers share the host OS kernel.
- Scalability: Easily scale containerized apps to handle increased demand.

## Core Docker Concepts
- Docker Images: A lightweight, standalone, and executable software package that includes everything needed to run a piece of software.
- Docker Containers: Instances of Docker images that run as isolated processes on a host machine.
- Dockerfile: A text file containing instructions to build a Docker image.
For a more detailed explanation, refer to Docker Overview (Official Docs).

## Requirements:
- Install Docker/Docker Desktop
  Install Docker on your local system or a cloud instance.
  Verify the installation with:
  ```sh
  docker --version
  ```

- Pull and Run a Container
  ```sh
  docker pull nginx
  ```
  ```sh
  docker run -d --name my-nginx -p 8080:80 nginx
  ```

- Inspect and Explore
  ```sh
  docker ps
  ```
  ```sh
  docker logs my-nginx
  ```
  ```sh
  docker inspect my-nginx
  ```

- Build a Custom Docker Image
  Download and save the provided index.html file to your project directory.
  Create a Dockerfile in the same directory with the following content:
  ```Dockerfile
  FROM nginx:latest
  COPY index.html /usr/share/nginx/html/index.html
  EXPOSE 80
  ```

  ```sh
  docker build -t my-nginx:custom .
  ```
  ```sh
  docker run -d --name my-custom-nginx -p 8081:80 my-nginx:custom
  ```

- Access and Test
  Open your browser and visit:
  - Default NGINX: http://localhost:8080
  - Custom NGINX: http://localhost:8081

- Docker Login
  ```sh
  docker login
  ```
  Enter your Docker Hub credentials when prompted.

- Push Image to Docker Hub
  ```sh
  docker tag my-nginx:custom <your-dockerhub-username>/my-nginx:custom
  docker push <your-dockerhub-username>/my-nginx:custom
  ```

- Pull Image from Docker Hub
  ```sh
  docker pull <your-dockerhub-username>/my-nginx:custom
  ```

- Troubleshooting Challenges
  Try running another container on the same port 8080. Observe and fix the issue.
  Stop a running container and attempt to access its application in the browser. What happens?
  Use the docker logs command to debug and restart a misconfigured container.
  Introduce an error in the Dockerfile (e.g., a typo in the COPY instruction). Build the image and fix the issue by reading the logs.

### Cleanup
- Stop and remove the containers:
```sh
  docker stop my-nginx my-custom-nginx
  docker rm my-nginx my-custom-nginx
```

- Remove the custom image:
```sh
  docker rmi my-nginx:custom
```


