#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS
from diagrams.aws.general import User
from diagrams.aws.network import APIGateway
from diagrams.k8s.compute import Pod

with Diagram("apiks", show=False):
    topic = User("client")

    with Cluster("AWS"):
        with Cluster("Node"):
            pod = Pod("Nginx")
            kong = APIGateway("Kong")
            flask = Pod("Flask")

        RDS = RDS("RDS PostgreSQL")

    topic >> pod
    pod >> kong >>flask
    flask >> RDS
