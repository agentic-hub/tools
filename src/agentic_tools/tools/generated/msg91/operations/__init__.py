# msg91 operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import Msg91Credentials

def get_tools() -> List[BaseTool]:
    """Get all msg91 operation tools."""
    tools = []
    from .send import Msg91SendTool
    tools.append(Msg91SendTool())
    return tools
