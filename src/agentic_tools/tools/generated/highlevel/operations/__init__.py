# highLevel operations
from typing import List
from langchain.tools import BaseTool
from .. import HighlevelCredentials

def get_tools() -> List[BaseTool]:
    """Get all highLevel operation tools."""
    tools = []
    from .create import HighlevelCreateTool
    tools.append(HighlevelCreateTool())
    from .delete import HighlevelDeleteTool
    tools.append(HighlevelDeleteTool())
    from .get import HighlevelGetTool
    tools.append(HighlevelGetTool())
    from .getall import HighlevelGetallTool
    tools.append(HighlevelGetallTool())
    from .lookup import HighlevelLookupTool
    tools.append(HighlevelLookupTool())
    from .update import HighlevelUpdateTool
    tools.append(HighlevelUpdateTool())
    from .__custom_api_call__ import Highlevel__custom_api_call__Tool
    tools.append(Highlevel__custom_api_call__Tool())
    from .create import HighlevelCreateTool
    tools.append(HighlevelCreateTool())
    from .delete import HighlevelDeleteTool
    tools.append(HighlevelDeleteTool())
    from .get import HighlevelGetTool
    tools.append(HighlevelGetTool())
    from .getall import HighlevelGetallTool
    tools.append(HighlevelGetallTool())
    from .update import HighlevelUpdateTool
    tools.append(HighlevelUpdateTool())
    from .__custom_api_call__ import Highlevel__custom_api_call__Tool
    tools.append(Highlevel__custom_api_call__Tool())
    from .create import HighlevelCreateTool
    tools.append(HighlevelCreateTool())
    from .delete import HighlevelDeleteTool
    tools.append(HighlevelDeleteTool())
    from .get import HighlevelGetTool
    tools.append(HighlevelGetTool())
    from .getall import HighlevelGetallTool
    tools.append(HighlevelGetallTool())
    from .update import HighlevelUpdateTool
    tools.append(HighlevelUpdateTool())
    from .__custom_api_call__ import Highlevel__custom_api_call__Tool
    tools.append(Highlevel__custom_api_call__Tool())
    return tools
