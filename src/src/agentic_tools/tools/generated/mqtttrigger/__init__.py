# mqttTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_mqtttrigger_tools() -> List[BaseTool]:
    """Get all mqttTrigger tools."""
    from . import operations
    return operations.get_tools()
