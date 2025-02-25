# payPal toolkit
from langchain.tools import BaseTool
from typing import List

def get_paypal_tools() -> List[BaseTool]:
    """Get all payPal tools."""
    from . import operations
    return operations.get_tools()
