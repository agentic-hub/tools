# formstackTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all formstackTrigger operation tools."""
    tools = []
    from .default import FormstacktriggerDefaultTool
    tools.append(FormstacktriggerDefaultTool())
    return tools
