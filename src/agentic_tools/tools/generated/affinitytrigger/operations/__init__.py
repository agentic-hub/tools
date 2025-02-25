# affinityTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all affinityTrigger operation tools."""
    tools = []
    from .default import AffinitytriggerDefaultTool
    tools.append(AffinitytriggerDefaultTool())
    return tools
