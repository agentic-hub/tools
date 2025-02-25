# mauticTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mauticTrigger operation tools."""
    tools = []
    from .default import MautictriggerDefaultTool
    tools.append(MautictriggerDefaultTool())
    return tools
