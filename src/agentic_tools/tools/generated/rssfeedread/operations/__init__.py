# rssFeedRead operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all rssFeedRead operation tools."""
    tools = []
    from .default import RssfeedreadDefaultTool
    tools.append(RssfeedreadDefaultTool())
    return tools
