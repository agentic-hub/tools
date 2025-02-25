# mocean operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mocean operation tools."""
    tools = []
    from .send import MoceanSendTool
    tools.append(MoceanSendTool())
    return tools
