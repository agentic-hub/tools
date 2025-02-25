# emeliaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all emeliaTrigger operation tools."""
    tools = []
    from .default import EmeliatriggerDefaultTool
    tools.append(EmeliatriggerDefaultTool())
    return tools
