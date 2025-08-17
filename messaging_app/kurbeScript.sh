#!/bin/bash

# start minekube using docker driver
minikube start --driver=docker

# Verify status of cluster
minekube status

kubectl cluster-info

# see single node in cluster
kubectl get nodeskurbeScript

# Retrieve the available pods
kubectl get pods
