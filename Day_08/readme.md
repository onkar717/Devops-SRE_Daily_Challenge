# Day 8 Challenge: Build a Distributed Logging System (Part1)

Hello EveryOne,

Welcome back to the DevOps SRE Daily Challenge! 🎉

Today, you’ll dive into distributed logging by setting up a centralized logging system. 
This hands-on challenge will help you understand the essentials of log management, message queues, and monitoring, all critical to modern DevOps practices.


## Requirements:
### Install and Configure Your Message Queue:
### Option A: RabbitMQ

### Install RabbitMQ:
```
sudo apt update sudo apt install rabbitmq-server -y
```
 
### Enable Management Plugin:
sudo rabbitmq-plugins enable rabbitmq_management
sudo systemctl restart rabbitmq-server
 
Access the RabbitMQ UI at http://<server-ip>:15672. Default credentials: guest/guest.

### Set Up a User and Queue:
```
sudo rabbitmqctl add_user your_username your_password sudo rabbitmqctl set_permissions -p / your_username ".*" ".*" ".*" sudo rabbitmqctl add_queue logs_queue
```
 
### Configure Network Access:
Edit /etc/rabbitmq/rabbitmq.conf to allow external access:
```
listeners.tcp.default = 5672
```

### Restart RabbitMQ:
```
sudo systemctl restart rabbitmq-server
```

### Option B: Redis

### Install Redis:
```
sudo apt update
sudo apt install redis-server -y
```

 
### Enable Authentication:
Edit /etc/redis/redis.conf and enable password authentication:
```
requirepass your_password
```

### Restart Redis:
```
sudo systemctl restart redis-server
```
 
### Configure Network Access:
Allow external access by modifying the bind setting in /etc/redis/redis.conf:
```
bind 0.0.0.0
```

### Restart Redis:
```
sudo systemctl restart redis-server
```


## Validation Steps
### For RabbitMQ:
```
Log in to the RabbitMQ management UI and verify the logs_queue exists.
Use the CLI to check the queue:
sudo rabbitmqctl list_queues
```

### For Redis:
Use the Redis CLI to verify the connection and authentication:
```
redis-cli -a your_password ping
Check the queue length:
redis-cli -a your_password LLEN logs_queue
```


