# taigaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all taigaTrigger operation tools."""
    tools = []
    from .default import TaigatriggerDefaultTool
    tools.append(TaigatriggerDefaultTool())
    return tools
