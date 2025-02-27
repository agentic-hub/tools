# convertToFile operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all convertToFile operation tools."""
    tools = []
    from .csv import ConverttofileCsvTool
    tools.append(ConverttofileCsvTool())
    from .html import ConverttofileHtmlTool
    tools.append(ConverttofileHtmlTool())
    from .ical import ConverttofileIcalTool
    tools.append(ConverttofileIcalTool())
    from .tojson import ConverttofileTojsonTool
    tools.append(ConverttofileTojsonTool())
    from .ods import ConverttofileOdsTool
    tools.append(ConverttofileOdsTool())
    from .rtf import ConverttofileRtfTool
    tools.append(ConverttofileRtfTool())
    from .xls import ConverttofileXlsTool
    tools.append(ConverttofileXlsTool())
    from .xlsx import ConverttofileXlsxTool
    tools.append(ConverttofileXlsxTool())
    from .tobinary import ConverttofileTobinaryTool
    tools.append(ConverttofileTobinaryTool())
    return tools
