# linkedIn operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import LinkedinCredentials

def get_tools() -> List[BaseTool]:
    """Get all linkedIn operation tools."""
    tools = []
    from .create import LinkedinCreateTool
    tools.append(LinkedinCreateTool())
    from .__custom_api_call__ import Linkedin__custom_api_call__Tool
    tools.append(Linkedin__custom_api_call__Tool())
    return tools
