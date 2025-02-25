# phantombuster operations
from typing import List
from langchain.tools import BaseTool
from .. import PhantombusterCredentials

def get_tools() -> List[BaseTool]:
    """Get all phantombuster operation tools."""
    tools = []
    from .delete import PhantombusterDeleteTool
    tools.append(PhantombusterDeleteTool())
    from .get import PhantombusterGetTool
    tools.append(PhantombusterGetTool())
    from .getall import PhantombusterGetallTool
    tools.append(PhantombusterGetallTool())
    from .getoutput import PhantombusterGetoutputTool
    tools.append(PhantombusterGetoutputTool())
    from .launch import PhantombusterLaunchTool
    tools.append(PhantombusterLaunchTool())
    from .__custom_api_call__ import Phantombuster__custom_api_call__Tool
    tools.append(Phantombuster__custom_api_call__Tool())
    return tools
