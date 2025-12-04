import boto3
import botocore.config
import json
from datetime import datetime


def blog_generate(blog_topic:str)->str:

    #prompt and body for llama model

    prompt = f"""
    Write a clear and engaging 200-word blog on: "{blog_topic}".
    Make it structured with an introduction, main section, and conclusion.
    """


    request_body = {
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.6,
        "top_p":0.9
    }
    ## Connect to bedrock
    try:

        bedrock = boto3.client("bedrock-runtime",
        region_name='us-east-1',
        config= botocore.config.Config(read_timeout=300, retries={'max_attempts': 3})
        )

        #invoke the model and convert the dict to json
        response = bedrock.invoke_model(
            body = json.dumps(request_body),
            modelId="us.meta.llama3-2-1b-instruct-v1:0"

        )
        #read the response o/p from streaming body
        response_bytes = response["body"].read()

        #convert the bytes -> dict
        response_dict = json.loads(response_bytes)
        blog_text = response_dict['generation']

        return blog_text
    
    except Exception as e:
        print(f"Error generating blog: {e}")
        return ""


def save_blogtos3(s3_key, s3_bucket, blog_text):

    s3 = boto3.client("s3")

    try:

        s3.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=blog_text
        )
        print(f"Blog saved to S3")
    
    except Exception as e:
        print(f"Error saving blog to S3: {e}")


def lambda_handler(event, context):
# API sent to lambda handler the event as str but we need to convert it to dict
    
    # body = json.loads(event['body'])
    # blogtopic = body['blogtopic']
    if "body" in event:
        body = json.loads(event["body"])
    else:
        body = event

    blogtopic = body["blogtopic"]

    blog_text  = blog_generate(blogtopic)

    if blog_text:
        current_time = datetime.now().strftime("%H%M%S")
        s3_key = f"blog-output/{current_time}.txt"
        s3_bucket = 'awsbedrockblogsanjay'

        save_blogtos3(s3_key, s3_bucket, blog_text)
    else:
        print("Error: Failed to generate blog")

    return {
        "statusCode":200,
        "body":json.dumps("Blog generated successfully")

    }