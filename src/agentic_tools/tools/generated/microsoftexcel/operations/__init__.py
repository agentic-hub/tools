# microsoftExcel operations
from typing import List
from langchain.tools import BaseTool
from .. import MicrosoftexcelCredentials

def get_tools() -> List[BaseTool]:
    """Get all microsoftExcel operation tools."""
    tools = []
    from .append import MicrosoftexcelAppendTool
    tools.append(MicrosoftexcelAppendTool())
    from .converttorange import MicrosoftexcelConverttorangeTool
    tools.append(MicrosoftexcelConverttorangeTool())
    from .addtable import MicrosoftexcelAddtableTool
    tools.append(MicrosoftexcelAddtableTool())
    from .deletetable import MicrosoftexcelDeletetableTool
    tools.append(MicrosoftexcelDeletetableTool())
    from .getcolumns import MicrosoftexcelGetcolumnsTool
    tools.append(MicrosoftexcelGetcolumnsTool())
    from .getrows import MicrosoftexcelGetrowsTool
    tools.append(MicrosoftexcelGetrowsTool())
    from .lookup import MicrosoftexcelLookupTool
    tools.append(MicrosoftexcelLookupTool())
    from .addworksheet import MicrosoftexcelAddworksheetTool
    tools.append(MicrosoftexcelAddworksheetTool())
    from .deleteworkbook import MicrosoftexcelDeleteworkbookTool
    tools.append(MicrosoftexcelDeleteworkbookTool())
    from .getall import MicrosoftexcelGetallTool
    tools.append(MicrosoftexcelGetallTool())
    from .append import MicrosoftexcelAppendTool
    tools.append(MicrosoftexcelAppendTool())
    from .upsert import MicrosoftexcelUpsertTool
    tools.append(MicrosoftexcelUpsertTool())
    from .clear import MicrosoftexcelClearTool
    tools.append(MicrosoftexcelClearTool())
    from .deleteworksheet import MicrosoftexcelDeleteworksheetTool
    tools.append(MicrosoftexcelDeleteworksheetTool())
    from .getall import MicrosoftexcelGetallTool
    tools.append(MicrosoftexcelGetallTool())
    from .readrows import MicrosoftexcelReadrowsTool
    tools.append(MicrosoftexcelReadrowsTool())
    from .update import MicrosoftexcelUpdateTool
    tools.append(MicrosoftexcelUpdateTool())
    return tools
