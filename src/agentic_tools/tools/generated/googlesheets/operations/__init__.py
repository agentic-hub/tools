# googleSheets operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GooglesheetsCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleSheets operation tools."""
    tools = []
    from .appendorupdate import GooglesheetsAppendorupdateTool
    tools.append(GooglesheetsAppendorupdateTool())
    from .append import GooglesheetsAppendTool
    tools.append(GooglesheetsAppendTool())
    from .clear import GooglesheetsClearTool
    tools.append(GooglesheetsClearTool())
    from .create import GooglesheetsCreateTool
    tools.append(GooglesheetsCreateTool())
    from .remove import GooglesheetsRemoveTool
    tools.append(GooglesheetsRemoveTool())
    from .delete import GooglesheetsDeleteTool
    tools.append(GooglesheetsDeleteTool())
    from .read import GooglesheetsReadTool
    tools.append(GooglesheetsReadTool())
    from .update import GooglesheetsUpdateTool
    tools.append(GooglesheetsUpdateTool())
    from .create import GooglesheetsCreateTool
    tools.append(GooglesheetsCreateTool())
    from .deletespreadsheet import GooglesheetsDeletespreadsheetTool
    tools.append(GooglesheetsDeletespreadsheetTool())
    return tools
