# mandrill operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MandrillCredentials

def get_tools() -> List[BaseTool]:
    """Get all mandrill operation tools."""
    tools = []
    from .sendtemplate import MandrillSendtemplateTool
    tools.append(MandrillSendtemplateTool())
    from .sendhtml import MandrillSendhtmlTool
    tools.append(MandrillSendhtmlTool())
    return tools
