# noOp operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all noOp operation tools."""
    tools = []
    from .default import NoopDefaultTool
    tools.append(NoopDefaultTool())
    return tools
