import docker

client = docker.from_env()

print("Pulling images:")
image = client.images.pull("alpine")
print(f"Image Tag: {image.tags}")
image = client.images.pull("ubuntu")
print(f"Image Tag: {image.tags}")


print("\nImages:")
for image in client.images.list():
    print(f"{image.tags}")

print("\nLaunching a containers:")
container1 = client.containers.run(
    "alpine",
    name = "Alpine_container",
    detach = True
)

container2 = client.containers.run(
    "ubuntu",
    name = "Ubuntu_container",
    detach = True
)

print(f"Container Name: {container1.name, container2.name}")
print(f"Container ID: {container1.id, container2.id}")