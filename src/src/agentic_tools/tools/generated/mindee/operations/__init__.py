# mindee operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mindee operation tools."""
    tools = []
    from .predict import MindeePredictTool
    tools.append(MindeePredictTool())
    from .__custom_api_call__ import Mindee__custom_api_call__Tool
    tools.append(Mindee__custom_api_call__Tool())
    return tools
