# dateTime operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel

def get_tools() -> List[BaseTool]:
    """Get all dateTime operation tools."""
    tools = []
    from .addtodate import DatetimeAddtodateTool
    tools.append(DatetimeAddtodateTool())
    from .extractdate import DatetimeExtractdateTool
    tools.append(DatetimeExtractdateTool())
    from .formatdate import DatetimeFormatdateTool
    tools.append(DatetimeFormatdateTool())
    from .getcurrentdate import DatetimeGetcurrentdateTool
    tools.append(DatetimeGetcurrentdateTool())
    from .gettimebetweendates import DatetimeGettimebetweendatesTool
    tools.append(DatetimeGettimebetweendatesTool())
    from .rounddate import DatetimeRounddateTool
    tools.append(DatetimeRounddateTool())
    from .subtractfromdate import DatetimeSubtractfromdateTool
    tools.append(DatetimeSubtractfromdateTool())
    return tools
