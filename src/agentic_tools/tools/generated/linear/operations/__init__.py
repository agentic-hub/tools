# linear operations
from typing import List
from langchain.tools import BaseTool
from .. import LinearCredentials

def get_tools() -> List[BaseTool]:
    """Get all linear operation tools."""
    tools = []
    from .create import LinearCreateTool
    tools.append(LinearCreateTool())
    from .delete import LinearDeleteTool
    tools.append(LinearDeleteTool())
    from .get import LinearGetTool
    tools.append(LinearGetTool())
    from .getall import LinearGetallTool
    tools.append(LinearGetallTool())
    from .update import LinearUpdateTool
    tools.append(LinearUpdateTool())
    from .__custom_api_call__ import Linear__custom_api_call__Tool
    tools.append(Linear__custom_api_call__Tool())
    return tools
