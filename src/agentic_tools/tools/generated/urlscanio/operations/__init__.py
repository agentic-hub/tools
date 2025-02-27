# urlScanIo operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import UrlscanioCredentials

def get_tools() -> List[BaseTool]:
    """Get all urlScanIo operation tools."""
    tools = []
    from .get import UrlscanioGetTool
    tools.append(UrlscanioGetTool())
    from .getall import UrlscanioGetallTool
    tools.append(UrlscanioGetallTool())
    from .perform import UrlscanioPerformTool
    tools.append(UrlscanioPerformTool())
    from .__custom_api_call__ import Urlscanio__custom_api_call__Tool
    tools.append(Urlscanio__custom_api_call__Tool())
    return tools
