# merge operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all merge operation tools."""
    tools = []
    from .default import MergeDefaultTool
    tools.append(MergeDefaultTool())
    return tools
