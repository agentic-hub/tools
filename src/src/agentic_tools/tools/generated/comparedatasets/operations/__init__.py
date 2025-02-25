# compareDatasets operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all compareDatasets operation tools."""
    tools = []
    from .default import ComparedatasetsDefaultTool
    tools.append(ComparedatasetsDefaultTool())
    return tools
