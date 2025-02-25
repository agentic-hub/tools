# typeformTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all typeformTrigger operation tools."""
    tools = []
    from .default import TypeformtriggerDefaultTool
    tools.append(TypeformtriggerDefaultTool())
    return tools
