# rocketchat operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import RocketchatCredentials

def get_tools() -> List[BaseTool]:
    """Get all rocketchat operation tools."""
    tools = []
    from .postmessage import RocketchatPostmessageTool
    tools.append(RocketchatPostmessageTool())
    from .__custom_api_call__ import Rocketchat__custom_api_call__Tool
    tools.append(Rocketchat__custom_api_call__Tool())
    return tools
