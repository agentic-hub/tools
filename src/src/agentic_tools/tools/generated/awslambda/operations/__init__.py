# awsLambda operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsLambda operation tools."""
    tools = []
    from .invoke import AwslambdaInvokeTool
    tools.append(AwslambdaInvokeTool())
    from .__custom_api_call__ import Awslambda__custom_api_call__Tool
    tools.append(Awslambda__custom_api_call__Tool())
    return tools
