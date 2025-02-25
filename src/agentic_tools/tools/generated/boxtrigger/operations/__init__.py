# boxTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all boxTrigger operation tools."""
    tools = []
    from .default import BoxtriggerDefaultTool
    tools.append(BoxtriggerDefaultTool())
    return tools
