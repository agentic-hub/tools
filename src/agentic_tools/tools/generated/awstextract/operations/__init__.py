# awsTextract operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import AwstextractCredentials

def get_tools() -> List[BaseTool]:
    """Get all awsTextract operation tools."""
    tools = []
    from .analyzeexpense import AwstextractAnalyzeexpenseTool
    tools.append(AwstextractAnalyzeexpenseTool())
    from .__custom_api_call__ import Awstextract__custom_api_call__Tool
    tools.append(Awstextract__custom_api_call__Tool())
    return tools
