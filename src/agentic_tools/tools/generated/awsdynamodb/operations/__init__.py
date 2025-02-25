# awsDynamoDb operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsDynamoDb operation tools."""
    tools = []
    from .upsert import AwsdynamodbUpsertTool
    tools.append(AwsdynamodbUpsertTool())
    from .delete import AwsdynamodbDeleteTool
    tools.append(AwsdynamodbDeleteTool())
    from .get import AwsdynamodbGetTool
    tools.append(AwsdynamodbGetTool())
    from .getall import AwsdynamodbGetallTool
    tools.append(AwsdynamodbGetallTool())
    from .__custom_api_call__ import Awsdynamodb__custom_api_call__Tool
    tools.append(Awsdynamodb__custom_api_call__Tool())
    return tools
