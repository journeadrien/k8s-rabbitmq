deploy-redis:
	kubectl replace --force -f redis.deployment.yaml

build-worker:
	docker build -t worker-job:v1 job
deploy-worker:build-worker
	kubectl replace --force -f worker-deployment.yaml
log-worker:
	kubectl logs -l app=worker

build-job:
	docker build -t redis-job:v1 job
launch-job: build-job
	kubectl replace --force -f job.yaml

pods=$(shell kubectl get pods --selector=job-name=job1 --output=jsonpath='{.items[*].metadata.name}')
log-job:
	kubectl logs $(pods)
