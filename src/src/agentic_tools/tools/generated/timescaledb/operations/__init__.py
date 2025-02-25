# timescaleDb operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all timescaleDb operation tools."""
    tools = []
    from .executequery import TimescaledbExecutequeryTool
    tools.append(TimescaledbExecutequeryTool())
    from .insert import TimescaledbInsertTool
    tools.append(TimescaledbInsertTool())
    from .update import TimescaledbUpdateTool
    tools.append(TimescaledbUpdateTool())
    return tools
