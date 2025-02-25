# sendInBlueTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendinbluetrigger_tools() -> List[BaseTool]:
    """Get all sendInBlueTrigger tools."""
    from . import operations
    return operations.get_tools()
