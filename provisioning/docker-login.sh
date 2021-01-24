#!/usr/bin/env bash

## Performs login to the registry provisioned with terraform

REGISTRY_NAME=$(cd ecr; terraform show -json | jq -r '.values.root_module.resources[].values.repository_url')
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 
