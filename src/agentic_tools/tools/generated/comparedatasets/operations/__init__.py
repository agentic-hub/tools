# compareDatasets operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all compareDatasets operation tools."""
    tools = []
    from .default import ComparedatasetsDefaultTool
    tools.append(ComparedatasetsDefaultTool())
    return tools
