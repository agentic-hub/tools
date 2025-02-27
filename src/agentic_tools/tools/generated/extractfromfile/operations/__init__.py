# extractFromFile operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all extractFromFile operation tools."""
    tools = []
    from .csv import ExtractfromfileCsvTool
    tools.append(ExtractfromfileCsvTool())
    from .html import ExtractfromfileHtmlTool
    tools.append(ExtractfromfileHtmlTool())
    from .fromjson import ExtractfromfileFromjsonTool
    tools.append(ExtractfromfileFromjsonTool())
    from .fromics import ExtractfromfileFromicsTool
    tools.append(ExtractfromfileFromicsTool())
    from .ods import ExtractfromfileOdsTool
    tools.append(ExtractfromfileOdsTool())
    from .pdf import ExtractfromfilePdfTool
    tools.append(ExtractfromfilePdfTool())
    from .rtf import ExtractfromfileRtfTool
    tools.append(ExtractfromfileRtfTool())
    from .text import ExtractfromfileTextTool
    tools.append(ExtractfromfileTextTool())
    from .xml import ExtractfromfileXmlTool
    tools.append(ExtractfromfileXmlTool())
    from .xls import ExtractfromfileXlsTool
    tools.append(ExtractfromfileXlsTool())
    from .xlsx import ExtractfromfileXlsxTool
    tools.append(ExtractfromfileXlsxTool())
    from .binarytopropery import ExtractfromfileBinarytoproperyTool
    tools.append(ExtractfromfileBinarytoproperyTool())
    return tools
