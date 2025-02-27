# shopify operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import ShopifyCredentials

def get_tools() -> List[BaseTool]:
    """Get all shopify operation tools."""
    tools = []
    from .create import ShopifyCreateTool
    tools.append(ShopifyCreateTool())
    from .delete import ShopifyDeleteTool
    tools.append(ShopifyDeleteTool())
    from .get import ShopifyGetTool
    tools.append(ShopifyGetTool())
    from .getall import ShopifyGetallTool
    tools.append(ShopifyGetallTool())
    from .update import ShopifyUpdateTool
    tools.append(ShopifyUpdateTool())
    from .__custom_api_call__ import Shopify__custom_api_call__Tool
    tools.append(Shopify__custom_api_call__Tool())
    from .create import ShopifyCreateTool
    tools.append(ShopifyCreateTool())
    from .delete import ShopifyDeleteTool
    tools.append(ShopifyDeleteTool())
    from .get import ShopifyGetTool
    tools.append(ShopifyGetTool())
    from .getall import ShopifyGetallTool
    tools.append(ShopifyGetallTool())
    from .update import ShopifyUpdateTool
    tools.append(ShopifyUpdateTool())
    from .__custom_api_call__ import Shopify__custom_api_call__Tool
    tools.append(Shopify__custom_api_call__Tool())
    return tools
