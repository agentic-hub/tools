# crateDb operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all crateDb operation tools."""
    tools = []
    from .executequery import CratedbExecutequeryTool
    tools.append(CratedbExecutequeryTool())
    from .insert import CratedbInsertTool
    tools.append(CratedbInsertTool())
    from .update import CratedbUpdateTool
    tools.append(CratedbUpdateTool())
    return tools
