# microsoftSql operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import MicrosoftsqlCredentials

def get_tools() -> List[BaseTool]:
    """Get all microsoftSql operation tools."""
    tools = []
    from .executequery import MicrosoftsqlExecutequeryTool
    tools.append(MicrosoftsqlExecutequeryTool())
    from .insert import MicrosoftsqlInsertTool
    tools.append(MicrosoftsqlInsertTool())
    from .update import MicrosoftsqlUpdateTool
    tools.append(MicrosoftsqlUpdateTool())
    from .delete import MicrosoftsqlDeleteTool
    tools.append(MicrosoftsqlDeleteTool())
    return tools
