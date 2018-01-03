import docker
client = docker.from_env()
#for container in client.containers.list():
#    print(container.id)
#    for containers in container.id:
#    container = container.id
#    print container.logs() will print out container logs
#print(client.images.list())

print(client.containers.list()) #will list the running containers
#container = client.containers.get('a4ecaa6bc2')
print(container.attrs['Config']['Image'])
print(container.logs())
for line in container.logs(stream=True):
    print(line.strip())

print(client.swarm.attrs())
