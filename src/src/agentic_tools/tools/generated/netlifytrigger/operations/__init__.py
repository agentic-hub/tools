# netlifyTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all netlifyTrigger operation tools."""
    tools = []
    from .default import NetlifytriggerDefaultTool
    tools.append(NetlifytriggerDefaultTool())
    return tools
