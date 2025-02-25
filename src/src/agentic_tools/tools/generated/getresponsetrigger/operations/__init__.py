# getResponseTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all getResponseTrigger operation tools."""
    tools = []
    from .default import GetresponsetriggerDefaultTool
    tools.append(GetresponsetriggerDefaultTool())
    return tools
