# plivo operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PlivoCredentials

def get_tools() -> List[BaseTool]:
    """Get all plivo operation tools."""
    tools = []
    from .send import PlivoSendTool
    tools.append(PlivoSendTool())
    from .send import PlivoSendTool
    tools.append(PlivoSendTool())
    from .make import PlivoMakeTool
    tools.append(PlivoMakeTool())
    return tools
