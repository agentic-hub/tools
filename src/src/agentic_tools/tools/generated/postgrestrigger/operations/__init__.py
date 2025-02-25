# postgresTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all postgresTrigger operation tools."""
    tools = []
    from .default import PostgrestriggerDefaultTool
    tools.append(PostgrestriggerDefaultTool())
    return tools
