# getResponse operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all getResponse operation tools."""
    tools = []
    from .create import GetresponseCreateTool
    tools.append(GetresponseCreateTool())
    from .delete import GetresponseDeleteTool
    tools.append(GetresponseDeleteTool())
    from .get import GetresponseGetTool
    tools.append(GetresponseGetTool())
    from .getall import GetresponseGetallTool
    tools.append(GetresponseGetallTool())
    from .update import GetresponseUpdateTool
    tools.append(GetresponseUpdateTool())
    from .__custom_api_call__ import Getresponse__custom_api_call__Tool
    tools.append(Getresponse__custom_api_call__Tool())
    return tools
