# awsComprehend operations
from typing import List
from langchain.tools import BaseTool

def get_tools() -> List[BaseTool]:
    """Get all awsComprehend operation tools."""
    tools = []
    from .detectdominantlanguage import AwscomprehendDetectdominantlanguageTool
    tools.append(AwscomprehendDetectdominantlanguageTool())
    from .detectentities import AwscomprehendDetectentitiesTool
    tools.append(AwscomprehendDetectentitiesTool())
    from .detectsentiment import AwscomprehendDetectsentimentTool
    tools.append(AwscomprehendDetectsentimentTool())
    from .__custom_api_call__ import Awscomprehend__custom_api_call__Tool
    tools.append(Awscomprehend__custom_api_call__Tool())
    return tools
