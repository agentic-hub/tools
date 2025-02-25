# awsRekognition toolkit
from langchain.tools import BaseTool
from typing import List

def get_awsrekognition_tools() -> List[BaseTool]:
    """Get all awsRekognition tools."""
    from . import operations
    return operations.get_tools()
