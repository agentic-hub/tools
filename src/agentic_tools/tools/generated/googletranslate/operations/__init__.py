# googleTranslate operations
from typing import List
from langchain.tools import BaseTool
from .. import GoogletranslateCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleTranslate operation tools."""
    tools = []
    from .translate import GoogletranslateTranslateTool
    tools.append(GoogletranslateTranslateTool())
    from .__custom_api_call__ import Googletranslate__custom_api_call__Tool
    tools.append(Googletranslate__custom_api_call__Tool())
    return tools
