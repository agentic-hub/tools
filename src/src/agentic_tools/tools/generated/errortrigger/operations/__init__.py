# errorTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all errorTrigger operation tools."""
    tools = []
    from .default import ErrortriggerDefaultTool
    tools.append(ErrortriggerDefaultTool())
    return tools
