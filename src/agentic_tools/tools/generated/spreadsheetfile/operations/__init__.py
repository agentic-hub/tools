# spreadsheetFile operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all spreadsheetFile operation tools."""
    tools = []
    from .fromfile import SpreadsheetfileFromfileTool
    tools.append(SpreadsheetfileFromfileTool())
    from .tofile import SpreadsheetfileTofileTool
    tools.append(SpreadsheetfileTofileTool())
    return tools
