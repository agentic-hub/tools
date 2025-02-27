# questDb operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import QuestdbCredentials

def get_tools() -> List[BaseTool]:
    """Get all questDb operation tools."""
    tools = []
    from .executequery import QuestdbExecutequeryTool
    tools.append(QuestdbExecutequeryTool())
    from .insert import QuestdbInsertTool
    tools.append(QuestdbInsertTool())
    return tools
