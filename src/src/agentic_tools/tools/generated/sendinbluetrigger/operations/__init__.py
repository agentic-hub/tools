# sendInBlueTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all sendInBlueTrigger operation tools."""
    tools = []
    from .default import SendinbluetriggerDefaultTool
    tools.append(SendinbluetriggerDefaultTool())
    return tools
