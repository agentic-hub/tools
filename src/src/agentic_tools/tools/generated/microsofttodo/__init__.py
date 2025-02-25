# microsoftToDo toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsofttodo_tools() -> List[BaseTool]:
    """Get all microsoftToDo tools."""
    from . import operations
    return operations.get_tools()
