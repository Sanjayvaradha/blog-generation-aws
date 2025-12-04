Blog generation AWS

A fully serverless AI-powered blog generation system using AWS Lambda, API Gateway (REST API), Amazon Bedrock, and a Streamlit UI.
Users can enter any topic and automatically generate a structured 200-word blog using an LLM (Llama 3 / chosen Bedrock model).

🚀 Features

✔ Serverless architecture (no EC2 required)
✔ Secure REST API with API Key protection
✔ AWS Lambda integration with Amazon Bedrock Runtime
✔ Generates high-quality blogs using LLMs
✔ Saves generated blogs automatically to Amazon S3
✔ Frontend UI built with Streamlit
✔ Easy to extend, deploy, and scale

This project uses:

✔ API Gateway REST API
✔ API Key
✔ Usage Plan
✔ Throttling (5 req/sec)
✔ Quota limit (100 req/day)

## ☁️ Deployment Architecture
This project was deployed on AWS Cloud using the following infrastructure:

* **Compute:** AWS EC2 (t2.micro/Ubuntu) for hosting the Streamlit frontend.
* **Backend:** AWS Lambda for serverless execution of the generation logic.
* **AI Model:** AWS Bedrock (Llama 3) for LLM text generation.
* **Storage:** AWS S3 for saving the generated blog posts.


### Deployment Steps Taken
1.  Provisioned EC2 instance (Ubuntu Image).
2.  Configured Security Groups (Inbound rules for Port 8501 and SSH).
3.  Connected via SSH and set up the Python environment.
