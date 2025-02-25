# googleContacts operations
from typing import List
from langchain.tools import BaseTool
from .. import GooglecontactsCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleContacts operation tools."""
    tools = []
    from .create import GooglecontactsCreateTool
    tools.append(GooglecontactsCreateTool())
    from .delete import GooglecontactsDeleteTool
    tools.append(GooglecontactsDeleteTool())
    from .get import GooglecontactsGetTool
    tools.append(GooglecontactsGetTool())
    from .getall import GooglecontactsGetallTool
    tools.append(GooglecontactsGetallTool())
    from .update import GooglecontactsUpdateTool
    tools.append(GooglecontactsUpdateTool())
    from .__custom_api_call__ import Googlecontacts__custom_api_call__Tool
    tools.append(Googlecontacts__custom_api_call__Tool())
    return tools
