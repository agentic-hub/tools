# removeDuplicates operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all removeDuplicates operation tools."""
    tools = []
    from .default import RemoveduplicatesDefaultTool
    tools.append(RemoveduplicatesDefaultTool())
    return tools
