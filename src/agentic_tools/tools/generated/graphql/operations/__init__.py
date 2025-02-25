# graphql operations
from typing import List
from langchain.tools import BaseTool
from .. import GraphqlCredentials

def get_tools() -> List[BaseTool]:
    """Get all graphql operation tools."""
    tools = []
    from .default import GraphqlDefaultTool
    tools.append(GraphqlDefaultTool())
    return tools
