# uproc operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all uproc operation tools."""
    tools = []
    from .default import UprocDefaultTool
    tools.append(UprocDefaultTool())
    return tools
