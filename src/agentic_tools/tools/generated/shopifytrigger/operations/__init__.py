# shopifyTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all shopifyTrigger operation tools."""
    tools = []
    from .default import ShopifytriggerDefaultTool
    tools.append(ShopifytriggerDefaultTool())
    return tools
