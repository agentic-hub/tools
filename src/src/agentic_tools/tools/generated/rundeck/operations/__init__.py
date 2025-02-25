# rundeck operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all rundeck operation tools."""
    tools = []
    from .execute import RundeckExecuteTool
    tools.append(RundeckExecuteTool())
    from .getmetadata import RundeckGetmetadataTool
    tools.append(RundeckGetmetadataTool())
    from .__custom_api_call__ import Rundeck__custom_api_call__Tool
    tools.append(Rundeck__custom_api_call__Tool())
    return tools
