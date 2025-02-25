# totp operations
from typing import List
from langchain.tools import BaseTool
from .. import TotpCredentials

def get_tools() -> List[BaseTool]:
    """Get all totp operation tools."""
    tools = []
    from .generatesecret import TotpGeneratesecretTool
    tools.append(TotpGeneratesecretTool())
    return tools
