# mySql operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all mySql operation tools."""
    tools = []
    from .deletetable import MysqlDeletetableTool
    tools.append(MysqlDeletetableTool())
    from .executequery import MysqlExecutequeryTool
    tools.append(MysqlExecutequeryTool())
    from .insert import MysqlInsertTool
    tools.append(MysqlInsertTool())
    from .upsert import MysqlUpsertTool
    tools.append(MysqlUpsertTool())
    from .select import MysqlSelectTool
    tools.append(MysqlSelectTool())
    from .update import MysqlUpdateTool
    tools.append(MysqlUpdateTool())
    return tools
