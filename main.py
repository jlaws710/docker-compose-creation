import yaml

def create_service():
    service = {}

    name = input("Enter service name: ").strip()
    image = input(f"Enter image for {name}: ").strip()

    service["image"] = image

    ports = input(f"Enter ports for {name} (format: host:container,comma separated or blank): ").strip()
    if ports:
        service["ports"] = [p.strip() for p in ports.split(",")]

    envs = {}
    while True:
        env_input = input("Add environment variable (key=value) or press enter to skip: ").strip()
        if not env_input:
            break
        if "=" in env_input:
            key, value = env_input.split("=", 1)
            envs[key.strip()] = value.strip()
    if envs:
        service["environment"] = envs

    volumes = input(f"Enter volumes for {name} (format: host_path:container_path,comma separated or blank): ").strip()
    if volumes:
        service["volumes"] = [v.strip() for v in volumes.split(",")]

    return name, service


def main():
    docker_compose = {
        "version": "4.1",
        "services": {}
    }

    while True:
        name, service = create_service()
        docker_compose["services"][name] = service

        more = input("Do you want to add another service? (y/n): ").strip().lower()
        if more != "y":
            break

    file_name = input("Enter output file name (default: docker-compose.yml): ").strip()
    if not file_name:
        file_name = "docker-compose.yml"

    with open(file_name, "w") as f:
        yaml.dump(docker_compose, f, sort_keys=False)

    print(f"\n✅ Docker Compose file '{file_name}' created successfully!")


if __name__ == "__main__":
    main()