# YOLO Kubeflow Training Pipeline

This repository contains a compiled Kubeflow pipeline and the infrastructure to deploy it automatically using a Docker image and Kubernetes job.

## Structure

- `Dockerfile`: Builds a container that runs the pipeline automatically
- `scripts/kbf.py`: Python script that authenticates and runs the pipeline via KFP SDK
- `pipeline.yaml`: Compiled KFP v2 pipeline definition
- `manifests/`: K8s Job and Kustomize setup to launch the container# yolo-pipeline
