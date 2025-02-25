# googleDocs operations
from typing import List
from langchain.tools import BaseTool
from .. import GoogledocsCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleDocs operation tools."""
    tools = []
    from .create import GoogledocsCreateTool
    tools.append(GoogledocsCreateTool())
    from .get import GoogledocsGetTool
    tools.append(GoogledocsGetTool())
    from .update import GoogledocsUpdateTool
    tools.append(GoogledocsUpdateTool())
    from .__custom_api_call__ import Googledocs__custom_api_call__Tool
    tools.append(Googledocs__custom_api_call__Tool())
    return tools
