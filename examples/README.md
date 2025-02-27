# Agentic Tools Examples

This directory contains examples of how to use the Agentic Tools library.

## AWS S3 Agent Example

The `s3.py` example demonstrates how to use the AWS S3 toolkit to interact with Amazon S3 buckets. It shows common operations like:

- Listing all S3 buckets
- Creating a new bucket
- Uploading files to a bucket
- Listing objects in a bucket
- Downloading files from a bucket
- Deleting files from a bucket
- Deleting buckets

### Prerequisites

Before running the example, make sure you have:

1. AWS credentials with appropriate permissions to perform S3 operations
2. Python 3.8 or higher
3. Required Python packages installed (see below)

### Setup

1. Create a `.env` file in the root directory with your AWS credentials:

```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=your_aws_region
OPENAI_API_KEY=your_openai_api_key
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Example

To run the S3 agent example:

```bash
python examples/s3.py
```

The example will:

1. Load AWS credentials from environment variables
2. Create an S3 agent with the appropriate tools
3. Demonstrate various S3 operations
4. Clean up any resources created during the demonstration

### Understanding the Code

The example is structured as follows:

- `load_aws_credentials()`: Loads AWS credentials from environment variables
- `create_s3_agent()`: Creates a LangChain agent with S3 tools
- `demonstrate_s3_operations()`: Demonstrates various S3 operations
- `main()`: Main function that runs the example

The S3 agent uses the following components:

- `AwsS3Toolkit`: Provides tools for interacting with AWS S3
- `Awss3Credentials`: Stores AWS credentials for authentication
- `ChatOpenAI`: LangChain language model for the agent
- `initialize_agent`: Creates a LangChain agent with the S3 tools

### Customizing the Example

You can customize the example by:

- Changing the language model used by the agent
- Adding more S3 operations
- Modifying the agent's behavior
- Integrating with other AWS services

### Troubleshooting

If you encounter issues:

1. Ensure your AWS credentials are correct and have the necessary permissions
2. Check that all required environment variables are set
3. Verify that you have the latest version of the Agentic Tools library
4. Look for error messages in the logs for more information 