# travisCi toolkit
from langchain.tools import BaseTool
from typing import List

def get_travisci_tools() -> List[BaseTool]:
    """Get all travisCi tools."""
    from . import operations
    return operations.get_tools()
