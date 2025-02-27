# googleBigQuery operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GooglebigqueryCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleBigQuery operation tools."""
    tools = []
    from .executequery import GooglebigqueryExecutequeryTool
    tools.append(GooglebigqueryExecutequeryTool())
    from .insert import GooglebigqueryInsertTool
    tools.append(GooglebigqueryInsertTool())
    from .__custom_api_call__ import Googlebigquery__custom_api_call__Tool
    tools.append(Googlebigquery__custom_api_call__Tool())
    return tools
