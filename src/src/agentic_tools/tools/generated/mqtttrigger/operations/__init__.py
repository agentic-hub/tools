# mqttTrigger operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mqttTrigger operation tools."""
    tools = []
    from .default import MqtttriggerDefaultTool
    tools.append(MqtttriggerDefaultTool())
    return tools
