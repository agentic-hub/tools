# lemlistTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all lemlistTrigger operation tools."""
    tools = []
    from .default import LemlisttriggerDefaultTool
    tools.append(LemlisttriggerDefaultTool())
    return tools
