# awsSnsTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsSnsTrigger operation tools."""
    tools = []
    from .default import AwssnstriggerDefaultTool
    tools.append(AwssnstriggerDefaultTool())
    return tools
