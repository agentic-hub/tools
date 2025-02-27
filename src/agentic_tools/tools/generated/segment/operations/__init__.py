# segment operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import SegmentCredentials

def get_tools() -> List[BaseTool]:
    """Get all segment operation tools."""
    tools = []
    from .add import SegmentAddTool
    tools.append(SegmentAddTool())
    from .__custom_api_call__ import Segment__custom_api_call__Tool
    tools.append(Segment__custom_api_call__Tool())
    from .create import SegmentCreateTool
    tools.append(SegmentCreateTool())
    from .__custom_api_call__ import Segment__custom_api_call__Tool
    tools.append(Segment__custom_api_call__Tool())
    from .event import SegmentEventTool
    tools.append(SegmentEventTool())
    from .page import SegmentPageTool
    tools.append(SegmentPageTool())
    from .__custom_api_call__ import Segment__custom_api_call__Tool
    tools.append(Segment__custom_api_call__Tool())
    return tools
