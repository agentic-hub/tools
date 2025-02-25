# html operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all html operation tools."""
    tools = []
    from .generatehtmltemplate import HtmlGeneratehtmltemplateTool
    tools.append(HtmlGeneratehtmltemplateTool())
    from .extracthtmlcontent import HtmlExtracthtmlcontentTool
    tools.append(HtmlExtracthtmlcontentTool())
    from .converttohtmltable import HtmlConverttohtmltableTool
    tools.append(HtmlConverttohtmltableTool())
    return tools
