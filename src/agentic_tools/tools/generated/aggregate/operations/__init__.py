# aggregate operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all aggregate operation tools."""
    tools = []
    from .default import AggregateDefaultTool
    tools.append(AggregateDefaultTool())
    return tools
