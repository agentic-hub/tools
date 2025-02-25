# splitInBatches toolkit
from langchain.tools import BaseTool
from typing import List

def get_splitinbatches_tools() -> List[BaseTool]:
    """Get all splitInBatches tools."""
    from . import operations
    return operations.get_tools()
