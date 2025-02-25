# contentful operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all contentful operation tools."""
    tools = []
    from .get import ContentfulGetTool
    tools.append(ContentfulGetTool())
    from .get import ContentfulGetTool
    tools.append(ContentfulGetTool())
    from .get import ContentfulGetTool
    tools.append(ContentfulGetTool())
    from .getall import ContentfulGetallTool
    tools.append(ContentfulGetallTool())
    from .get import ContentfulGetTool
    tools.append(ContentfulGetTool())
    from .getall import ContentfulGetallTool
    tools.append(ContentfulGetallTool())
    from .getall import ContentfulGetallTool
    tools.append(ContentfulGetallTool())
    return tools
