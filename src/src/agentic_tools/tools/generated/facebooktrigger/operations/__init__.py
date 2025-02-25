# facebookTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all facebookTrigger operation tools."""
    tools = []
    from .default import FacebooktriggerDefaultTool
    tools.append(FacebooktriggerDefaultTool())
    return tools
