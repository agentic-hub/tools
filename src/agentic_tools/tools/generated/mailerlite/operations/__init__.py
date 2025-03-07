# mailerLite operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MailerliteCredentials

def get_tools() -> List[BaseTool]:
    """Get all mailerLite operation tools."""
    tools = []
    from .create import MailerliteCreateTool
    tools.append(MailerliteCreateTool())
    from .get import MailerliteGetTool
    tools.append(MailerliteGetTool())
    from .getall import MailerliteGetallTool
    tools.append(MailerliteGetallTool())
    from .update import MailerliteUpdateTool
    tools.append(MailerliteUpdateTool())
    return tools
