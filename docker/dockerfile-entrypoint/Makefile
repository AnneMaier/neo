build: 
	docker build -t ctop .
run: 
	docker run -it ctop
run2:
	docker run -it ctop -d 2
exec: 
	docker exec -it cmds /bin/bash
ps: 
	docker ps -a
img: 
	docker images
rm: 
	docker rm $(docker ps -aq)
rmi: 
	docker rmi $$(docker images -q)
