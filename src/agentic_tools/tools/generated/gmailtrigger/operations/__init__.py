# gmailTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all gmailTrigger operation tools."""
    tools = []
    from .default import GmailtriggerDefaultTool
    tools.append(GmailtriggerDefaultTool())
    return tools
