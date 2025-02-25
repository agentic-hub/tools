# ciscoWebexTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all ciscoWebexTrigger operation tools."""
    tools = []
    from .default import CiscowebextriggerDefaultTool
    tools.append(CiscowebextriggerDefaultTool())
    return tools
