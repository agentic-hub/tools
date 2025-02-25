# customerIo operations
from typing import List
from langchain.tools import BaseTool
from .. import CustomerioCredentials

def get_tools() -> List[BaseTool]:
    """Get all customerIo operation tools."""
    tools = []
    from .get import CustomerioGetTool
    tools.append(CustomerioGetTool())
    from .getall import CustomerioGetallTool
    tools.append(CustomerioGetallTool())
    from .getmetrics import CustomerioGetmetricsTool
    tools.append(CustomerioGetmetricsTool())
    from .__custom_api_call__ import Customerio__custom_api_call__Tool
    tools.append(Customerio__custom_api_call__Tool())
    from .upsert import CustomerioUpsertTool
    tools.append(CustomerioUpsertTool())
    from .delete import CustomerioDeleteTool
    tools.append(CustomerioDeleteTool())
    from .__custom_api_call__ import Customerio__custom_api_call__Tool
    tools.append(Customerio__custom_api_call__Tool())
    from .track import CustomerioTrackTool
    tools.append(CustomerioTrackTool())
    from .trackanonymous import CustomerioTrackanonymousTool
    tools.append(CustomerioTrackanonymousTool())
    from .__custom_api_call__ import Customerio__custom_api_call__Tool
    tools.append(Customerio__custom_api_call__Tool())
    from .add import CustomerioAddTool
    tools.append(CustomerioAddTool())
    from .remove import CustomerioRemoveTool
    tools.append(CustomerioRemoveTool())
    from .__custom_api_call__ import Customerio__custom_api_call__Tool
    tools.append(Customerio__custom_api_call__Tool())
    return tools
