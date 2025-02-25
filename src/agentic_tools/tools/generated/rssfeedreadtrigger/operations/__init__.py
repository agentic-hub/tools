# rssFeedReadTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all rssFeedReadTrigger operation tools."""
    tools = []
    from .default import RssfeedreadtriggerDefaultTool
    tools.append(RssfeedreadtriggerDefaultTool())
    return tools
