# wooCommerceTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all wooCommerceTrigger operation tools."""
    tools = []
    from .default import WoocommercetriggerDefaultTool
    tools.append(WoocommercetriggerDefaultTool())
    return tools
