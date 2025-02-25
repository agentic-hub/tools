# summarize operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all summarize operation tools."""
    tools = []
    from .default import SummarizeDefaultTool
    tools.append(SummarizeDefaultTool())
    return tools
