# bitbucketTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all bitbucketTrigger operation tools."""
    tools = []
    from .default import BitbuckettriggerDefaultTool
    tools.append(BitbuckettriggerDefaultTool())
    return tools
