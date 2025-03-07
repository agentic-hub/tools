# snowflake operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import SnowflakeCredentials

def get_tools() -> List[BaseTool]:
    """Get all snowflake operation tools."""
    tools = []
    from .executequery import SnowflakeExecutequeryTool
    tools.append(SnowflakeExecutequeryTool())
    from .insert import SnowflakeInsertTool
    tools.append(SnowflakeInsertTool())
    from .update import SnowflakeUpdateTool
    tools.append(SnowflakeUpdateTool())
    return tools
