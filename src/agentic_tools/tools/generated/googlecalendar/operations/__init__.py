# googleCalendar operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import GooglecalendarCredentials

def get_tools() -> List[BaseTool]:
    """Get all googleCalendar operation tools."""
    tools = []
    from .availability import GooglecalendarAvailabilityTool
    tools.append(GooglecalendarAvailabilityTool())
    from .__custom_api_call__ import Googlecalendar__custom_api_call__Tool
    tools.append(Googlecalendar__custom_api_call__Tool())
    from .create import GooglecalendarCreateTool
    tools.append(GooglecalendarCreateTool())
    from .delete import GooglecalendarDeleteTool
    tools.append(GooglecalendarDeleteTool())
    from .get import GooglecalendarGetTool
    tools.append(GooglecalendarGetTool())
    from .getall import GooglecalendarGetallTool
    tools.append(GooglecalendarGetallTool())
    from .update import GooglecalendarUpdateTool
    tools.append(GooglecalendarUpdateTool())
    from .__custom_api_call__ import Googlecalendar__custom_api_call__Tool
    tools.append(Googlecalendar__custom_api_call__Tool())
    return tools
