# splitInBatches operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all splitInBatches operation tools."""
    tools = []
    from .default import SplitinbatchesDefaultTool
    tools.append(SplitinbatchesDefaultTool())
    return tools
