# strapi operations
from typing import List
from langchain.tools import BaseTool
from .. import StrapiCredentials

def get_tools() -> List[BaseTool]:
    """Get all strapi operation tools."""
    tools = []
    from .create import StrapiCreateTool
    tools.append(StrapiCreateTool())
    from .delete import StrapiDeleteTool
    tools.append(StrapiDeleteTool())
    from .get import StrapiGetTool
    tools.append(StrapiGetTool())
    from .getall import StrapiGetallTool
    tools.append(StrapiGetallTool())
    from .update import StrapiUpdateTool
    tools.append(StrapiUpdateTool())
    from .__custom_api_call__ import Strapi__custom_api_call__Tool
    tools.append(Strapi__custom_api_call__Tool())
    return tools
