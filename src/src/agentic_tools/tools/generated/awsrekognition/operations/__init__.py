# awsRekognition operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsRekognition operation tools."""
    tools = []
    from .analyze import AwsrekognitionAnalyzeTool
    tools.append(AwsrekognitionAnalyzeTool())
    from .__custom_api_call__ import Awsrekognition__custom_api_call__Tool
    tools.append(Awsrekognition__custom_api_call__Tool())
    return tools
