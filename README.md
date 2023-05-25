## Overview

Creating serverless apis using lambda, api gateway and dynamodb.

## Learning Objectives

The learning objectives of this task are: 
- To learn AWS Services: API Gateway.
- To write a RESTful API Gateway interface for web crawler CRUD operations.
- Store data in dynamodb table

## Technologies Used

Following are the AWS Serivices that I used:
-For this task, we have used the following technologies:
- AWS API gateway
- Boto3 resource and client
- AWS Lambda
- DynamoDB

## Getting Started
---

Following is the procedure to install `aws cdk` locally. We will use the Windows Subsystem for Linux and VS Code. 

### Environment Setup:
---

1. In the Windows PowerShell, type the following command to install Windows Subsystem for Linux (WSL):
    ```sh
    wsl –-install
    ```
2. Install [Remote Development](https://code.visualstudio.com/docs/remote/wsl-tutorial) extention in VS Code to run in WSL from there.
3. Open Ubuntu console and Install Python
    ```sh
    sudo apt update
    ```
    ```sh
    sudo apt install python3 python3-pip
    ```
    ```sh
    python3 --version
    ```
4. Run following commands in Ubuntu console to install AWS CLI V2
    ```sh
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    ```
    ```sh
    sudo apt install unzip
    ```
    ```sh
    unzip awscliv2.zip
    ```
    ```sh
    sudo ./aws/install
    ```
    ```sh
    aws --version

### Project Deployment:
---
To run this project in your local aws environment follow the below commands.

1. Run `git clone "url-to-github-repo"` in Ubuntu console.
2. Setup virtual environment
    ```sh
    python3 -m venv .venv && source .venv/bin/activate # If not already installed
    ```
3. Install requirments
    ```sh
    pip install -r requirements.aws.txt
    ```
4. Create cloud formation template
    ```sh
    cdk synth
    ```
5. Deploy cloud formation
   ```sh
   cdk deploy

## Useful Commands

* `cdk ls` list all stacks in the app
* `cdk synth` emits the synthesized CloudFormation template
* `cdk deploy` deploy the stack to your default aws account/region
* `cdk diff` compare deployed stack with current stack
* `cdk doc` opens cdk documentation


## API Reference

A list of all the references and resources used to build this project is here:
* [AWS IAM](https://docs.aws.amazon.com/iam/?id=docs_gateway)
* [AWS Lambda](https://docs.aws.amazon.com/lambda/?id=docs_gateway)
* [AWS DynamoDB](https://docs.aws.amazon.com/dynamodb/?id=docs_gateway)

