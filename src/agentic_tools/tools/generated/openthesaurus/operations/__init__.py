# openThesaurus operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all openThesaurus operation tools."""
    tools = []
    from .getsynonyms import OpenthesaurusGetsynonymsTool
    tools.append(OpenthesaurusGetsynonymsTool())
    return tools
