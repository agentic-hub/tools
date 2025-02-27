# totp operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import TotpCredentials

def get_tools() -> List[BaseTool]:
    """Get all totp operation tools."""
    tools = []
    from .generatesecret import TotpGeneratesecretTool
    tools.append(TotpGeneratesecretTool())
    return tools
