# convertKitTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all convertKitTrigger operation tools."""
    tools = []
    from .default import ConvertkittriggerDefaultTool
    tools.append(ConvertkittriggerDefaultTool())
    return tools
