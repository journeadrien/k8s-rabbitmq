# create a namespace
create-namespace:
	kubectl apply -f namespace.yaml

# create rabbitmq broker
# local registy: eval $(minikube docker-env)
deploy-rabbitmq:
	kubectl replace --force -f rabbitmq-definition.yaml
log-rabbitmq:
	kubectl logs rabbitmq-master-server-0 --tail=50 --namespace rabbitmq
ui-rabbitmq:
	kubectl -n rabbitmq port-forward "service/rabbitmq-master" 15672 &
# create worker
build-worker:
	docker build -t rabbitmq-worker:v1 worker
deploy-worker:build-worker
	kubectl replace --force -f worker-deployment.yaml
log-worker:
	kubectl logs --tail=50 -l app=worker --namespace rabbitmq
exec-worker:
	kubectl run -i --tty  redis-worker:v1 --image=rabbitmq-worker:v1 sh

# create job
build-job:
	docker build -t rabbitmq-job:v1 job
launch-job: build-job
	kubectl replace --force -f job.yaml
log-job:
	kubectl logs -f -l job-name=job1 -n rabbitmq
