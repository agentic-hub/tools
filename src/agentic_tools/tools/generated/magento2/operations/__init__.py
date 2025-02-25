# magento2 operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all magento2 operation tools."""
    tools = []
    from .create import Magento2CreateTool
    tools.append(Magento2CreateTool())
    from .delete import Magento2DeleteTool
    tools.append(Magento2DeleteTool())
    from .get import Magento2GetTool
    tools.append(Magento2GetTool())
    from .getall import Magento2GetallTool
    tools.append(Magento2GetallTool())
    from .update import Magento2UpdateTool
    tools.append(Magento2UpdateTool())
    from .__custom_api_call__ import Magento2__custom_api_call__Tool
    tools.append(Magento2__custom_api_call__Tool())
    from .create import Magento2CreateTool
    tools.append(Magento2CreateTool())
    from .__custom_api_call__ import Magento2__custom_api_call__Tool
    tools.append(Magento2__custom_api_call__Tool())
    from .cancel import Magento2CancelTool
    tools.append(Magento2CancelTool())
    from .get import Magento2GetTool
    tools.append(Magento2GetTool())
    from .getall import Magento2GetallTool
    tools.append(Magento2GetallTool())
    from .ship import Magento2ShipTool
    tools.append(Magento2ShipTool())
    from .__custom_api_call__ import Magento2__custom_api_call__Tool
    tools.append(Magento2__custom_api_call__Tool())
    from .create import Magento2CreateTool
    tools.append(Magento2CreateTool())
    from .delete import Magento2DeleteTool
    tools.append(Magento2DeleteTool())
    from .get import Magento2GetTool
    tools.append(Magento2GetTool())
    from .getall import Magento2GetallTool
    tools.append(Magento2GetallTool())
    from .update import Magento2UpdateTool
    tools.append(Magento2UpdateTool())
    from .__custom_api_call__ import Magento2__custom_api_call__Tool
    tools.append(Magento2__custom_api_call__Tool())
    return tools
