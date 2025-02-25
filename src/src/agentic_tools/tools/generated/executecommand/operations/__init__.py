# executeCommand operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all executeCommand operation tools."""
    tools = []
    from .default import ExecutecommandDefaultTool
    tools.append(ExecutecommandDefaultTool())
    return tools
