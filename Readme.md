# RabbitMQ Horizontal-Scaling on kubernetes cluster.

Auto-scaling of workers that receive messages from a job RabbitMQ queue. In this example a worker receives a Nasdaq Symbol and dowload some data with yahoo-finance. When adding a massive amount of queue messages, multiple pods opens and performed this simple tasks at a high speed.


## Prerequisites

1. Kubernetes cluster: Minikube for instance.
2. Registre docker pour minikube (qui tourne sur une VM hors de l'OS du host) `eval $(minikube docker-env)`

# Litterature
- Redis dashboard queue monitoring. (Redis+flask)[https://testdriven.io/blog/asynchronous-tasks-with-flask-and-redis-queue/]

- Explication avec du scaling (Java queue)[https://www.freecodecamp.org/news/how-to-scale-microservices-with-message-queues-spring-boot-and-kubernetes-f691b7ba3acf/]
