# googleAnalytics operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GoogleanalyticsCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleAnalytics operation tools."""
    tools = []
    from .get import GoogleanalyticsGetTool
    tools.append(GoogleanalyticsGetTool())
    from .__custom_api_call__ import Googleanalytics__custom_api_call__Tool
    tools.append(Googleanalytics__custom_api_call__Tool())
    from .search import GoogleanalyticsSearchTool
    tools.append(GoogleanalyticsSearchTool())
    from .__custom_api_call__ import Googleanalytics__custom_api_call__Tool
    tools.append(Googleanalytics__custom_api_call__Tool())
    return tools
