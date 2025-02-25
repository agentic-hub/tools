# theHiveTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all theHiveTrigger operation tools."""
    tools = []
    from .default import ThehivetriggerDefaultTool
    tools.append(ThehivetriggerDefaultTool())
    return tools
