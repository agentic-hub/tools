# mondayCom operations
from typing import List
from langchain.tools import BaseTool
from .. import MondaycomCredentials

def get_tools() -> List[BaseTool]:
    """Get all mondayCom operation tools."""
    tools = []
    from .archive import MondaycomArchiveTool
    tools.append(MondaycomArchiveTool())
    from .create import MondaycomCreateTool
    tools.append(MondaycomCreateTool())
    from .get import MondaycomGetTool
    tools.append(MondaycomGetTool())
    from .getall import MondaycomGetallTool
    tools.append(MondaycomGetallTool())
    from .__custom_api_call__ import Mondaycom__custom_api_call__Tool
    tools.append(Mondaycom__custom_api_call__Tool())
    from .create import MondaycomCreateTool
    tools.append(MondaycomCreateTool())
    from .getall import MondaycomGetallTool
    tools.append(MondaycomGetallTool())
    from .__custom_api_call__ import Mondaycom__custom_api_call__Tool
    tools.append(Mondaycom__custom_api_call__Tool())
    from .delete import MondaycomDeleteTool
    tools.append(MondaycomDeleteTool())
    from .create import MondaycomCreateTool
    tools.append(MondaycomCreateTool())
    from .getall import MondaycomGetallTool
    tools.append(MondaycomGetallTool())
    from .__custom_api_call__ import Mondaycom__custom_api_call__Tool
    tools.append(Mondaycom__custom_api_call__Tool())
    from .addupdate import MondaycomAddupdateTool
    tools.append(MondaycomAddupdateTool())
    from .changecolumnvalue import MondaycomChangecolumnvalueTool
    tools.append(MondaycomChangecolumnvalueTool())
    from .changemultiplecolumnvalues import MondaycomChangemultiplecolumnvaluesTool
    tools.append(MondaycomChangemultiplecolumnvaluesTool())
    from .create import MondaycomCreateTool
    tools.append(MondaycomCreateTool())
    from .delete import MondaycomDeleteTool
    tools.append(MondaycomDeleteTool())
    from .get import MondaycomGetTool
    tools.append(MondaycomGetTool())
    from .getbycolumnvalue import MondaycomGetbycolumnvalueTool
    tools.append(MondaycomGetbycolumnvalueTool())
    from .getall import MondaycomGetallTool
    tools.append(MondaycomGetallTool())
    from .move import MondaycomMoveTool
    tools.append(MondaycomMoveTool())
    from .__custom_api_call__ import Mondaycom__custom_api_call__Tool
    tools.append(Mondaycom__custom_api_call__Tool())
    return tools
