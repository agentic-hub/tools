# mailgun operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MailgunCredentials

def get_tools() -> List[BaseTool]:
    """Get all mailgun operation tools."""
    tools = []
    from .default import MailgunDefaultTool
    tools.append(MailgunDefaultTool())
    return tools
