"""A collection of functions to facilitate working with k8s in Python."""
from .kubetools import get_all, delete, top
from .gcloud import get_gcloud_node_info