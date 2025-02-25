# elasticsearch toolkit
from langchain.tools import BaseTool
from typing import List

def get_elasticsearch_tools() -> List[BaseTool]:
    """Get all elasticsearch tools."""
    from . import operations
    return operations.get_tools()
