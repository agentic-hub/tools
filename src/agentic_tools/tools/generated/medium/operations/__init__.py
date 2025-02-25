# medium operations
from typing import List
from langchain.tools import BaseTool
from .. import MediumCredentials

def get_tools() -> List[BaseTool]:
    """Get all medium operation tools."""
    tools = []
    from .create import MediumCreateTool
    tools.append(MediumCreateTool())
    from .__custom_api_call__ import Medium__custom_api_call__Tool
    tools.append(Medium__custom_api_call__Tool())
    from .getall import MediumGetallTool
    tools.append(MediumGetallTool())
    from .__custom_api_call__ import Medium__custom_api_call__Tool
    tools.append(Medium__custom_api_call__Tool())
    return tools
