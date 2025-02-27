#!/usr/bin/env python3
"""
AWS S3 Agent Example

This example demonstrates how to use the AWS S3 toolkit to interact with Amazon S3 buckets.
It shows common operations like listing buckets, uploading files, downloading files, and managing objects.
"""

import os
import sys
import logging
from typing import Dict, List
from dotenv import load_dotenv
from langchain.agents import (
    AgentExecutor,
    create_react_agent,
)
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.base import BaseTool

# Add the src directory to the path so we can import the agentic_tools package
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from agentic_tools.tools.generated.awss3 import AwsS3Toolkit, Awss3Credentials
from langchain_openai import ChatOpenAI

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_aws_credentials() -> Dict[str, str]:
    """
    Load AWS credentials from environment variables.

    Returns:
        Dict[str, str]: Dictionary containing AWS credentials
    """
    # Return proper AWS credentials format
    return {"id": 152}


def create_s3_agent(credentials: Dict[str, str], verbose: bool = False):
    """
    Create an agent that can interact with AWS S3.

    Args:
        credentials (Dict[str, str]): AWS credentials
        verbose (bool, optional): Whether to enable verbose output. Defaults to False.

    Returns:
        Agent: LangChain agent with S3 tools
    """
    # Create S3 credentials
    s3_credentials = Awss3Credentials(aws=credentials)

    # Initialize the S3 toolkit with credentials
    s3_toolkit = AwsS3Toolkit(credentials=s3_credentials)

    # Get tools and ensure they have proper names
    tools = s3_toolkit.get_tools()

    # Initialize the language model
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4o",
    )

    # Create a prompt template for the agent
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an assistant that helps users interact with AWS S3. Use the available tools to help users manage their S3 buckets and objects.\n\nTools: {tools}\n\nTool Names: {tool_names}",
            ),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor


def demonstrate_s3_operations(agent):
    """
    Demonstrate common S3 operations using the agent.

    Args:
        agent: LangChain agent with S3 tools
    """
    # Example 1: List all S3 buckets
    logger.info("Example 1: Listing all S3 buckets")
    result = agent.invoke({"input": "List all my S3 buckets"})
    logger.info(f"Result: {result['output']}")

    # Example 2: Create a new bucket
    bucket_name = "example-bucket-" + os.urandom(4).hex()
    logger.info(f"Example 2: Creating a new bucket named {bucket_name}")
    result = agent.invoke({"input": f"Create a new S3 bucket named {bucket_name}"})
    logger.info(f"Result: {result['output']}")

    # Example 3: Upload a file to the bucket
    logger.info(f"Example 3: Uploading a file to {bucket_name}")
    # Create a temporary file to upload
    with open("temp_file.txt", "w") as f:
        f.write("This is a test file for S3 upload")

    result = agent.invoke(
        {
            "input": f"Upload the file temp_file.txt to bucket {bucket_name} with the key 'test/temp_file.txt'"
        }
    )
    logger.info(f"Result: {result['output']}")

    # Example 4: List objects in the bucket
    logger.info(f"Example 4: Listing objects in bucket {bucket_name}")
    result = agent.invoke({"input": f"List all objects in bucket {bucket_name}"})
    logger.info(f"Result: {result['output']}")

    # Example 5: Download the file
    logger.info(f"Example 5: Downloading a file from bucket {bucket_name}")
    result = agent.invoke(
        {
            "input": f"Download the file with key 'test/temp_file.txt' from bucket {bucket_name}"
        }
    )
    logger.info(f"Result: {result['output']}")

    # Example 6: Delete the file
    logger.info(f"Example 6: Deleting a file from bucket {bucket_name}")
    result = agent.invoke(
        {
            "input": f"Delete the file with key 'test/temp_file.txt' from bucket {bucket_name}"
        }
    )
    logger.info(f"Result: {result['output']}")

    # Example 7: Delete the bucket
    logger.info(f"Example 7: Deleting bucket {bucket_name}")
    result = agent.invoke({"input": f"Delete the bucket named {bucket_name}"})
    logger.info(f"Result: {result['output']}")

    # Clean up
    if os.path.exists("temp_file.txt"):
        os.remove("temp_file.txt")


def main():
    # Load AWS credentials
    credentials = load_aws_credentials()

    # Create S3 agent
    agent = create_s3_agent(credentials, verbose=True)

    # Demonstrate S3 operations
    demonstrate_s3_operations(agent)


if __name__ == "__main__":
    main()
