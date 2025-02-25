# disqus operations
from typing import List
from langchain.tools import BaseTool
from .. import DisqusCredentials

def get_tools() -> List[BaseTool]:
    """Get all disqus operation tools."""
    tools = []
    from .get import DisqusGetTool
    tools.append(DisqusGetTool())
    from .getcategories import DisqusGetcategoriesTool
    tools.append(DisqusGetcategoriesTool())
    from .getthreads import DisqusGetthreadsTool
    tools.append(DisqusGetthreadsTool())
    from .getposts import DisqusGetpostsTool
    tools.append(DisqusGetpostsTool())
    return tools
