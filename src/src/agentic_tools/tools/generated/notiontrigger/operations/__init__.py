# notionTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all notionTrigger operation tools."""
    tools = []
    from .default import NotiontriggerDefaultTool
    tools.append(NotiontriggerDefaultTool())
    return tools
