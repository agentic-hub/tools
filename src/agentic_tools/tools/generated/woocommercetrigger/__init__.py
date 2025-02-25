# wooCommerceTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_woocommercetrigger_tools() -> List[BaseTool]:
    """Get all wooCommerceTrigger tools."""
    from . import operations
    return operations.get_tools()
