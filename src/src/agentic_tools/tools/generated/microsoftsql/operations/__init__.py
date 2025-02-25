# microsoftSql operations
from typing import List
from langchain.tools import BaseTool

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
