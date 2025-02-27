# wooCommerce operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import WoocommerceCredentials

def get_tools() -> List[BaseTool]:
    """Get all wooCommerce operation tools."""
    tools = []
    from .create import WoocommerceCreateTool
    tools.append(WoocommerceCreateTool())
    from .delete import WoocommerceDeleteTool
    tools.append(WoocommerceDeleteTool())
    from .get import WoocommerceGetTool
    tools.append(WoocommerceGetTool())
    from .getall import WoocommerceGetallTool
    tools.append(WoocommerceGetallTool())
    from .update import WoocommerceUpdateTool
    tools.append(WoocommerceUpdateTool())
    from .__custom_api_call__ import Woocommerce__custom_api_call__Tool
    tools.append(Woocommerce__custom_api_call__Tool())
    from .create import WoocommerceCreateTool
    tools.append(WoocommerceCreateTool())
    from .delete import WoocommerceDeleteTool
    tools.append(WoocommerceDeleteTool())
    from .get import WoocommerceGetTool
    tools.append(WoocommerceGetTool())
    from .getall import WoocommerceGetallTool
    tools.append(WoocommerceGetallTool())
    from .update import WoocommerceUpdateTool
    tools.append(WoocommerceUpdateTool())
    from .__custom_api_call__ import Woocommerce__custom_api_call__Tool
    tools.append(Woocommerce__custom_api_call__Tool())
    from .create import WoocommerceCreateTool
    tools.append(WoocommerceCreateTool())
    from .delete import WoocommerceDeleteTool
    tools.append(WoocommerceDeleteTool())
    from .get import WoocommerceGetTool
    tools.append(WoocommerceGetTool())
    from .getall import WoocommerceGetallTool
    tools.append(WoocommerceGetallTool())
    from .update import WoocommerceUpdateTool
    tools.append(WoocommerceUpdateTool())
    from .__custom_api_call__ import Woocommerce__custom_api_call__Tool
    tools.append(Woocommerce__custom_api_call__Tool())
    return tools
