# emailSend operations
from typing import List
from langchain.tools import BaseTool
from .. import EmailsendCredentials

def get_tools() -> List[BaseTool]:
    """Get all emailSend operation tools."""
    tools = []
    from .default import EmailsendDefaultTool
    tools.append(EmailsendDefaultTool())
    return tools
