# moveBinaryData operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all moveBinaryData operation tools."""
    tools = []
    from .default import MovebinarydataDefaultTool
    tools.append(MovebinarydataDefaultTool())
    return tools
