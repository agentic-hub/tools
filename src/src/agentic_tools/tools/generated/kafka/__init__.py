# kafka toolkit
from langchain.tools import BaseTool
from typing import List

def get_kafka_tools() -> List[BaseTool]:
    """Get all kafka tools."""
    from . import operations
    return operations.get_tools()
