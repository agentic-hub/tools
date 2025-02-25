# airtableTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all airtableTrigger operation tools."""
    tools = []
    from .default import AirtabletriggerDefaultTool
    tools.append(AirtabletriggerDefaultTool())
    return tools
