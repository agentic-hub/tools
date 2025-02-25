# freshworksCrm operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all freshworksCrm operation tools."""
    tools = []
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .query import FreshworkscrmQueryTool
    tools.append(FreshworkscrmQueryTool())
    from .lookup import FreshworkscrmLookupTool
    tools.append(FreshworkscrmLookupTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    from .create import FreshworkscrmCreateTool
    tools.append(FreshworkscrmCreateTool())
    from .delete import FreshworkscrmDeleteTool
    tools.append(FreshworkscrmDeleteTool())
    from .get import FreshworkscrmGetTool
    tools.append(FreshworkscrmGetTool())
    from .getall import FreshworkscrmGetallTool
    tools.append(FreshworkscrmGetallTool())
    from .update import FreshworkscrmUpdateTool
    tools.append(FreshworkscrmUpdateTool())
    from .__custom_api_call__ import Freshworkscrm__custom_api_call__Tool
    tools.append(Freshworkscrm__custom_api_call__Tool())
    return tools
