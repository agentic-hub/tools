# jotFormTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all jotFormTrigger operation tools."""
    tools = []
    from .default import JotformtriggerDefaultTool
    tools.append(JotformtriggerDefaultTool())
    return tools
