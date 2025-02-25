# awsLambda toolkit
from langchain.tools import BaseTool
from typing import List

def get_awslambda_tools() -> List[BaseTool]:
    """Get all awsLambda tools."""
    from . import operations
    return operations.get_tools()
