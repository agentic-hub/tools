# summarize operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all summarize operation tools."""
    tools = []
    from .default import SummarizeDefaultTool
    tools.append(SummarizeDefaultTool())
    return tools
