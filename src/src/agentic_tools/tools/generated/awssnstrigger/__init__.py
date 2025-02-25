# awsSnsTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_awssnstrigger_tools() -> List[BaseTool]:
    """Get all awsSnsTrigger tools."""
    from . import operations
    return operations.get_tools()
