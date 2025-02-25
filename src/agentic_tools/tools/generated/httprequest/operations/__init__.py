# httpRequest operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all httpRequest operation tools."""
    tools = []
    from .default import HttprequestDefaultTool
    tools.append(HttprequestDefaultTool())
    return tools
