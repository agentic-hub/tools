# postmarkTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all postmarkTrigger operation tools."""
    tools = []
    from .default import PostmarktriggerDefaultTool
    tools.append(PostmarktriggerDefaultTool())
    return tools
