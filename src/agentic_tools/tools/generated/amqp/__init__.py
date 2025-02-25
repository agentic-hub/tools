# amqp toolkit
from langchain.tools import BaseTool
from typing import List

def get_amqp_tools() -> List[BaseTool]:
    """Get all amqp tools."""
    from . import operations
    return operations.get_tools()
