# twist operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import TwistCredentials

def get_tools() -> List[BaseTool]:
    """Get all twist operation tools."""
    tools = []
    from .archive import TwistArchiveTool
    tools.append(TwistArchiveTool())
    from .create import TwistCreateTool
    tools.append(TwistCreateTool())
    from .delete import TwistDeleteTool
    tools.append(TwistDeleteTool())
    from .get import TwistGetTool
    tools.append(TwistGetTool())
    from .getall import TwistGetallTool
    tools.append(TwistGetallTool())
    from .unarchive import TwistUnarchiveTool
    tools.append(TwistUnarchiveTool())
    from .update import TwistUpdateTool
    tools.append(TwistUpdateTool())
    from .__custom_api_call__ import Twist__custom_api_call__Tool
    tools.append(Twist__custom_api_call__Tool())
    from .create import TwistCreateTool
    tools.append(TwistCreateTool())
    from .delete import TwistDeleteTool
    tools.append(TwistDeleteTool())
    from .get import TwistGetTool
    tools.append(TwistGetTool())
    from .getall import TwistGetallTool
    tools.append(TwistGetallTool())
    from .update import TwistUpdateTool
    tools.append(TwistUpdateTool())
    from .__custom_api_call__ import Twist__custom_api_call__Tool
    tools.append(Twist__custom_api_call__Tool())
    from .create import TwistCreateTool
    tools.append(TwistCreateTool())
    from .delete import TwistDeleteTool
    tools.append(TwistDeleteTool())
    from .get import TwistGetTool
    tools.append(TwistGetTool())
    from .getall import TwistGetallTool
    tools.append(TwistGetallTool())
    from .update import TwistUpdateTool
    tools.append(TwistUpdateTool())
    from .__custom_api_call__ import Twist__custom_api_call__Tool
    tools.append(Twist__custom_api_call__Tool())
    from .create import TwistCreateTool
    tools.append(TwistCreateTool())
    from .delete import TwistDeleteTool
    tools.append(TwistDeleteTool())
    from .get import TwistGetTool
    tools.append(TwistGetTool())
    from .getall import TwistGetallTool
    tools.append(TwistGetallTool())
    from .update import TwistUpdateTool
    tools.append(TwistUpdateTool())
    from .__custom_api_call__ import Twist__custom_api_call__Tool
    tools.append(Twist__custom_api_call__Tool())
    return tools
