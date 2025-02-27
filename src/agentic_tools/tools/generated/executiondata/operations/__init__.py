# executionData operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all executionData operation tools."""
    tools = []
    from .save import ExecutiondataSaveTool
    tools.append(ExecutiondataSaveTool())
    return tools
