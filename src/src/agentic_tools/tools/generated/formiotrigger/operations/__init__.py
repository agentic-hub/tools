# formIoTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all formIoTrigger operation tools."""
    tools = []
    from .default import FormiotriggerDefaultTool
    tools.append(FormiotriggerDefaultTool())
    return tools
