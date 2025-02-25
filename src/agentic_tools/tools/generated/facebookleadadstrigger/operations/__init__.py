# facebookLeadAdsTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all facebookLeadAdsTrigger operation tools."""
    tools = []
    from .default import FacebookleadadstriggerDefaultTool
    tools.append(FacebookleadadstriggerDefaultTool())
    return tools
