# crateDb toolkit
from langchain.tools import BaseTool
from typing import List

def get_cratedb_tools() -> List[BaseTool]:
    """Get all crateDb tools."""
    from . import operations
    return operations.get_tools()
