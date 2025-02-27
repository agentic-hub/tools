# aggregate operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all aggregate operation tools."""
    tools = []
    from .default import AggregateDefaultTool
    tools.append(AggregateDefaultTool())
    return tools
