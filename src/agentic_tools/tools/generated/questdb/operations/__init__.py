# questDb operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all questDb operation tools."""
    tools = []
    from .executequery import QuestdbExecutequeryTool
    tools.append(QuestdbExecutequeryTool())
    from .insert import QuestdbInsertTool
    tools.append(QuestdbInsertTool())
    return tools
