# pagerDuty toolkit
from langchain.tools import BaseTool
from typing import List

def get_pagerduty_tools() -> List[BaseTool]:
    """Get all pagerDuty tools."""
    from . import operations
    return operations.get_tools()
