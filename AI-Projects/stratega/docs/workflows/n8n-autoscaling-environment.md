# n8n Autoscaling Environment for Google Maps Scraper

This document summarizes the purpose and setup of the `n8n-autoscaling` repository found at [https://github.com/conor-is-my-name/n8n-autoscaling](https://github.com/conor-is-my-name/n8n-autoscaling).

## Overview

This repository **does not contain a downloadable n8n workflow**. Instead, it provides a complete, scalable environment using Docker to run n8n with a custom-built "Google Maps Scraper" node.

It is a template for creating a cost-effective, scalable, and resilient n8n setup using AWS EC2, Spot Instances, and Docker.

## Key Components

*   **`n8n-custom`**: A custom n8n Docker image that includes the `n8n-nodes-google-maps-scraper`.
*   **`n8n-worker`**: A service that handles the execution of n8n workflows.
*   **`gmaps-scraper`**: The FastAPI service for scraping Google Maps, documented in `google-maps-scraper-api.md`.
*   **`docker-compose.yml`**: The main file that defines and configures all the services, networks, and volumes to run the entire application stack.

## Setup and Usage

To use this, you would clone the repository and follow the instructions in its `README.md` to build and run the Docker containers. This would give you a running instance of n8n that has a new, custom "Google Maps Scraper" node available in the workflow editor.

You would then build a workflow inside that n8n instance to use the custom node.
