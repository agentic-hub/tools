# googlePerspective operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GoogleperspectiveCredentials

def get_tools() -> List[BaseTool]:
    """Get all googlePerspective operation tools."""
    tools = []
    from .analyzecomment import GoogleperspectiveAnalyzecommentTool
    tools.append(GoogleperspectiveAnalyzecommentTool())
    from .__custom_api_call__ import Googleperspective__custom_api_call__Tool
    tools.append(Googleperspective__custom_api_call__Tool())
    return tools
