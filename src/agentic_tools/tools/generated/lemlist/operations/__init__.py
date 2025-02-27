# lemlist operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import LemlistCredentials

def get_tools() -> List[BaseTool]:
    """Get all lemlist operation tools."""
    tools = []
    from .getall import LemlistGetallTool
    tools.append(LemlistGetallTool())
    from .__custom_api_call__ import Lemlist__custom_api_call__Tool
    tools.append(Lemlist__custom_api_call__Tool())
    from .getall import LemlistGetallTool
    tools.append(LemlistGetallTool())
    from .__custom_api_call__ import Lemlist__custom_api_call__Tool
    tools.append(Lemlist__custom_api_call__Tool())
    from .create import LemlistCreateTool
    tools.append(LemlistCreateTool())
    from .delete import LemlistDeleteTool
    tools.append(LemlistDeleteTool())
    from .get import LemlistGetTool
    tools.append(LemlistGetTool())
    from .unsubscribe import LemlistUnsubscribeTool
    tools.append(LemlistUnsubscribeTool())
    from .__custom_api_call__ import Lemlist__custom_api_call__Tool
    tools.append(Lemlist__custom_api_call__Tool())
    from .get import LemlistGetTool
    tools.append(LemlistGetTool())
    from .__custom_api_call__ import Lemlist__custom_api_call__Tool
    tools.append(Lemlist__custom_api_call__Tool())
    from .add import LemlistAddTool
    tools.append(LemlistAddTool())
    from .delete import LemlistDeleteTool
    tools.append(LemlistDeleteTool())
    from .getall import LemlistGetallTool
    tools.append(LemlistGetallTool())
    from .__custom_api_call__ import Lemlist__custom_api_call__Tool
    tools.append(Lemlist__custom_api_call__Tool())
    return tools
