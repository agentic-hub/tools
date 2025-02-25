# amqpTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_amqptrigger_tools() -> List[BaseTool]:
    """Get all amqpTrigger tools."""
    from . import operations
    return operations.get_tools()
