# coda operations
from typing import List
from langchain.tools import BaseTool
from .. import CodaCredentials

def get_tools() -> List[BaseTool]:
    """Get all coda operation tools."""
    tools = []
    from .createrow import CodaCreaterowTool
    tools.append(CodaCreaterowTool())
    from .deleterow import CodaDeleterowTool
    tools.append(CodaDeleterowTool())
    from .getallcolumns import CodaGetallcolumnsTool
    tools.append(CodaGetallcolumnsTool())
    from .getallrows import CodaGetallrowsTool
    tools.append(CodaGetallrowsTool())
    from .getcolumn import CodaGetcolumnTool
    tools.append(CodaGetcolumnTool())
    from .getrow import CodaGetrowTool
    tools.append(CodaGetrowTool())
    from .pushbutton import CodaPushbuttonTool
    tools.append(CodaPushbuttonTool())
    from .get import CodaGetTool
    tools.append(CodaGetTool())
    from .getall import CodaGetallTool
    tools.append(CodaGetallTool())
    from .get import CodaGetTool
    tools.append(CodaGetTool())
    from .getall import CodaGetallTool
    tools.append(CodaGetallTool())
    from .deleteviewrow import CodaDeleteviewrowTool
    tools.append(CodaDeleteviewrowTool())
    from .get import CodaGetTool
    tools.append(CodaGetTool())
    from .getallviewcolumns import CodaGetallviewcolumnsTool
    tools.append(CodaGetallviewcolumnsTool())
    from .getall import CodaGetallTool
    tools.append(CodaGetallTool())
    from .getallviewrows import CodaGetallviewrowsTool
    tools.append(CodaGetallviewrowsTool())
    from .pushviewbutton import CodaPushviewbuttonTool
    tools.append(CodaPushviewbuttonTool())
    from .updateviewrow import CodaUpdateviewrowTool
    tools.append(CodaUpdateviewrowTool())
    return tools
