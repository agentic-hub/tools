# splitInBatches operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all splitInBatches operation tools."""
    tools = []
    from .default import SplitinbatchesDefaultTool
    tools.append(SplitinbatchesDefaultTool())
    return tools
