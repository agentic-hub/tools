# googleSheetsTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all googleSheetsTrigger operation tools."""
    tools = []
    from .default import GooglesheetstriggerDefaultTool
    tools.append(GooglesheetstriggerDefaultTool())
    return tools
