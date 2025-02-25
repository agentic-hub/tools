# asanaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all asanaTrigger operation tools."""
    tools = []
    from .default import AsanatriggerDefaultTool
    tools.append(AsanatriggerDefaultTool())
    return tools
