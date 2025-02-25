# kafkaTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all kafkaTrigger operation tools."""
    tools = []
    from .default import KafkatriggerDefaultTool
    tools.append(KafkatriggerDefaultTool())
    return tools
