# postgres operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import PostgresCredentials

def get_tools() -> List[BaseTool]:
    """Get all postgres operation tools."""
    tools = []
    from .deletetable import PostgresDeletetableTool
    tools.append(PostgresDeletetableTool())
    from .executequery import PostgresExecutequeryTool
    tools.append(PostgresExecutequeryTool())
    from .insert import PostgresInsertTool
    tools.append(PostgresInsertTool())
    from .upsert import PostgresUpsertTool
    tools.append(PostgresUpsertTool())
    from .select import PostgresSelectTool
    tools.append(PostgresSelectTool())
    from .update import PostgresUpdateTool
    tools.append(PostgresUpdateTool())
    return tools
