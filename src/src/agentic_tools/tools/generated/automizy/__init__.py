# automizy toolkit
from langchain.tools import BaseTool
from typing import List

def get_automizy_tools() -> List[BaseTool]:
    """Get all automizy tools."""
    from . import operations
    return operations.get_tools()
