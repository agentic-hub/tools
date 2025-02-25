# jiraTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all jiraTrigger operation tools."""
    tools = []
    from .default import JiratriggerDefaultTool
    tools.append(JiratriggerDefaultTool())
    return tools
