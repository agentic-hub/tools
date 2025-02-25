# mailcheck operations
from typing import List
from langchain.tools import BaseTool
from .. import MailcheckCredentials

def get_tools() -> List[BaseTool]:
    """Get all mailcheck operation tools."""
    tools = []
    from .check import MailcheckCheckTool
    tools.append(MailcheckCheckTool())
    return tools
