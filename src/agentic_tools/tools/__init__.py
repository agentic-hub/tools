from .base import *
from .generated import *

# Tools package
# Import all toolkit classes from generated
# Usage examples:
# 1. With default credentials:
#    from agentic_tools.tools import S3Toolkit
#    tools = S3Toolkit().get_tools()
#
# 2. With custom credentials:
#    from agentic_tools.tools import S3Toolkit, S3Credentials
#    credentials = S3Credentials(
#        aws_access_key_id='your-access-key',
#        aws_secret_access_key='your-secret-key',
#        region_name='us-west-2'
#    )
#    tools = S3Toolkit(credentials=credentials).get_tools()
#
# 3. Using with LangChain:
#    from langchain.agents import initialize_agent
#    from langchain.llms import OpenAI
#    from agentic_tools.tools import S3Toolkit
#
#    llm = OpenAI(temperature=0)
#    tools = S3Toolkit().get_tools()
#    agent = initialize_agent(tools, llm, agent='zero-shot-react-description')
