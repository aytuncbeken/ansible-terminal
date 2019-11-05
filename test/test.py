import docker

def test():
    print("Started testing..")

    d_client = docker.from_env
    d_client


def init_docker_images():
    d_client = docker.from_env()




if __name__ == '__main__':
    test()