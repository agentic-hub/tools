# hackerNews operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all hackerNews operation tools."""
    tools = []
    from .getall import HackernewsGetallTool
    tools.append(HackernewsGetallTool())
    from .get import HackernewsGetTool
    tools.append(HackernewsGetTool())
    from .get import HackernewsGetTool
    tools.append(HackernewsGetTool())
    return tools
