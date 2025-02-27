# hackerNews operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

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
