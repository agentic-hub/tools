# mqtt operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MqttCredentials

def get_tools() -> List[BaseTool]:
    """Get all mqtt operation tools."""
    tools = []
    from .default import MqttDefaultTool
    tools.append(MqttDefaultTool())
    return tools
