build:
	docker build -t ubuntu:x .
run:
	docker run -it --name ubuntu -d -p 8000:80 ubuntu:x
exec:
	docker exec -it ubuntu /bin/bash
ps:
	docker ps -a
img:
	docker images
rm:
	docker stop $$(docker ps -aq)
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
