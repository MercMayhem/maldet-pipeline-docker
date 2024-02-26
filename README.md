# Malware Detection Pipeline Docker Image
Dockerizing my [malware detection pipeline](https://github.com/MercMayhem/malware-detection-pipeline).

## Requirement
Have AWS configured on host system. We will be passing on the credentials to the container to use. 

**WARNING**: Only run this where no other user can access the container.

## Installation
1. Clone this repository locally: 
	`git clone https://github.com/MercMayhem/maldet-pipeline-docker.git`
2. Build the image
	`docker build -t <image_name> /path/to/repository/`
3. Navigate to the source code and build it:
	`sudo cargo build`
	
## Run
You can run program using both `docker container run` as well as using the `compose.yaml` present in the repo.

1. Using `docker container run`:

    ```
    docker container run docker container run -e SERVER_URI="<Enter Server URI>" -v $HOME/.aws/credentials:/root/.aws/credentials  -v <path to config.yaml>:/config.yaml -v <path to schema.yaml>:/schema.yaml -v <path to params.yaml>:/params.yaml <name of image>
    ```

2. Using `docker compose`:
	
	Modify the image and source URI, config.yaml, params.yaml and schema.yaml fields to your liking then run:
	```
	docker compose up
	```
