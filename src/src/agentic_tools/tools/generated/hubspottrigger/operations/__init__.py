# hubspotTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all hubspotTrigger operation tools."""
    tools = []
    from .default import HubspottriggerDefaultTool
    tools.append(HubspottriggerDefaultTool())
    return tools
