# loneScale operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all loneScale operation tools."""
    tools = []
    from .create import LonescaleCreateTool
    tools.append(LonescaleCreateTool())
    from .__custom_api_call__ import Lonescale__custom_api_call__Tool
    tools.append(Lonescale__custom_api_call__Tool())
    from .add import LonescaleAddTool
    tools.append(LonescaleAddTool())
    from .__custom_api_call__ import Lonescale__custom_api_call__Tool
    tools.append(Lonescale__custom_api_call__Tool())
    return tools
