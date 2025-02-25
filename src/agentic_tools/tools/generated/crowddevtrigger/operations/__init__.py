# crowdDevTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all crowdDevTrigger operation tools."""
    tools = []
    from .default import CrowddevtriggerDefaultTool
    tools.append(CrowddevtriggerDefaultTool())
    return tools
