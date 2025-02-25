# signl4 operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all signl4 operation tools."""
    tools = []
    from .send import Signl4SendTool
    tools.append(Signl4SendTool())
    from .resolve import Signl4ResolveTool
    tools.append(Signl4ResolveTool())
    return tools
