# executeCommand operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all executeCommand operation tools."""
    tools = []
    from .default import ExecutecommandDefaultTool
    tools.append(ExecutecommandDefaultTool())
    return tools
