# markdown operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all markdown operation tools."""
    tools = []
    from .default import MarkdownDefaultTool
    tools.append(MarkdownDefaultTool())
    return tools
