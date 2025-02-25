# asana operations
from typing import List
from langchain.tools import BaseTool
from .. import AsanaCredentials

def get_tools() -> List[BaseTool]:
    """Get all asana operation tools."""
    tools = []
    from .create import AsanaCreateTool
    tools.append(AsanaCreateTool())
    from .getall import AsanaGetallTool
    tools.append(AsanaGetallTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .create import AsanaCreateTool
    tools.append(AsanaCreateTool())
    from .delete import AsanaDeleteTool
    tools.append(AsanaDeleteTool())
    from .get import AsanaGetTool
    tools.append(AsanaGetTool())
    from .getall import AsanaGetallTool
    tools.append(AsanaGetallTool())
    from .move import AsanaMoveTool
    tools.append(AsanaMoveTool())
    from .search import AsanaSearchTool
    tools.append(AsanaSearchTool())
    from .update import AsanaUpdateTool
    tools.append(AsanaUpdateTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .add import AsanaAddTool
    tools.append(AsanaAddTool())
    from .remove import AsanaRemoveTool
    tools.append(AsanaRemoveTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .add import AsanaAddTool
    tools.append(AsanaAddTool())
    from .remove import AsanaRemoveTool
    tools.append(AsanaRemoveTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .add import AsanaAddTool
    tools.append(AsanaAddTool())
    from .remove import AsanaRemoveTool
    tools.append(AsanaRemoveTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .get import AsanaGetTool
    tools.append(AsanaGetTool())
    from .getall import AsanaGetallTool
    tools.append(AsanaGetallTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    from .create import AsanaCreateTool
    tools.append(AsanaCreateTool())
    from .delete import AsanaDeleteTool
    tools.append(AsanaDeleteTool())
    from .get import AsanaGetTool
    tools.append(AsanaGetTool())
    from .getall import AsanaGetallTool
    tools.append(AsanaGetallTool())
    from .update import AsanaUpdateTool
    tools.append(AsanaUpdateTool())
    from .__custom_api_call__ import Asana__custom_api_call__Tool
    tools.append(Asana__custom_api_call__Tool())
    return tools
