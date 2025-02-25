# pipedriveTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all pipedriveTrigger operation tools."""
    tools = []
    from .default import PipedrivetriggerDefaultTool
    tools.append(PipedrivetriggerDefaultTool())
    return tools
