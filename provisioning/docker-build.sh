#!/usr/bin/env bash

## Builds image to the registry provisioned with terraform

set -e
REGISTRY_NAME=$(cd ecr; terraform show -json | jq -r '.values.root_module.resources[].values.repository_url')
docker build -t apiks docker-eks-deploy
docker tag apiks:latest $REGISTRY_NAME:latest
docker push $REGISTRY_NAME:latest
