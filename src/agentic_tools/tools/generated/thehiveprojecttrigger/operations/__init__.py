# theHiveProjectTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all theHiveProjectTrigger operation tools."""
    tools = []
    from .default import ThehiveprojecttriggerDefaultTool
    tools.append(ThehiveprojecttriggerDefaultTool())
    return tools
