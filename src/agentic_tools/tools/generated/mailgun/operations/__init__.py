# mailgun operations
from typing import List
from langchain.tools import BaseTool
from .. import MailgunCredentials

def get_tools() -> List[BaseTool]:
    """Get all mailgun operation tools."""
    tools = []
    from .default import MailgunDefaultTool
    tools.append(MailgunDefaultTool())
    return tools
