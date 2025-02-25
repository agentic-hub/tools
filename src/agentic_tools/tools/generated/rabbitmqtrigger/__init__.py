# rabbitmqTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_rabbitmqtrigger_tools() -> List[BaseTool]:
    """Get all rabbitmqTrigger tools."""
    from . import operations
    return operations.get_tools()
