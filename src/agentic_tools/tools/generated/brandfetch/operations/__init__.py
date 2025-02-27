# Brandfetch operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import BrandfetchCredentials

def get_tools() -> List[BaseTool]:
    """Get all Brandfetch operation tools."""
    tools = []
    from .color import BrandfetchColorTool
    tools.append(BrandfetchColorTool())
    from .company import BrandfetchCompanyTool
    tools.append(BrandfetchCompanyTool())
    from .font import BrandfetchFontTool
    tools.append(BrandfetchFontTool())
    from .industry import BrandfetchIndustryTool
    tools.append(BrandfetchIndustryTool())
    from .logo import BrandfetchLogoTool
    tools.append(BrandfetchLogoTool())
    return tools
