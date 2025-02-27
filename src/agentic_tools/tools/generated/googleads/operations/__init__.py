# googleAds operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GoogleadsCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleAds operation tools."""
    tools = []
    from .getall import GoogleadsGetallTool
    tools.append(GoogleadsGetallTool())
    from .get import GoogleadsGetTool
    tools.append(GoogleadsGetTool())
    from .__custom_api_call__ import Googleads__custom_api_call__Tool
    tools.append(Googleads__custom_api_call__Tool())
    return tools
