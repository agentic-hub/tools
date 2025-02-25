# googleCloudNaturalLanguage operations
from typing import List
from langchain.tools import BaseTool
from .. import GooglecloudnaturallanguageCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleCloudNaturalLanguage operation tools."""
    tools = []
    from .analyzesentiment import GooglecloudnaturallanguageAnalyzesentimentTool
    tools.append(GooglecloudnaturallanguageAnalyzesentimentTool())
    from .__custom_api_call__ import Googlecloudnaturallanguage__custom_api_call__Tool
    tools.append(Googlecloudnaturallanguage__custom_api_call__Tool())
    return tools
