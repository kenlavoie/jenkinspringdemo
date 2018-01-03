import docker
client = docker.from_env()
print client.containers.run("ubuntu:xenail", tty=True, interactive=True)

import docker 
client = docker.from_env()
for container in client.containers.list():
    print container.id
    #container = container.id
    #print container.logs() will print out container logs
