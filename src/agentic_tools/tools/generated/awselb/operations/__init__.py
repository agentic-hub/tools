# awsElb operations
from typing import List
from agentic_tools.tools import BaseTool, BaseModel
from .. import AwselbCredentials

def get_tools() -> List[BaseTool]:
    """Get all awsElb operation tools."""
    tools = []
    from .create import AwselbCreateTool
    tools.append(AwselbCreateTool())
    from .delete import AwselbDeleteTool
    tools.append(AwselbDeleteTool())
    from .get import AwselbGetTool
    tools.append(AwselbGetTool())
    from .getmany import AwselbGetmanyTool
    tools.append(AwselbGetmanyTool())
    from .__custom_api_call__ import Awselb__custom_api_call__Tool
    tools.append(Awselb__custom_api_call__Tool())
    from .add import AwselbAddTool
    tools.append(AwselbAddTool())
    from .getmany import AwselbGetmanyTool
    tools.append(AwselbGetmanyTool())
    from .remove import AwselbRemoveTool
    tools.append(AwselbRemoveTool())
    from .__custom_api_call__ import Awselb__custom_api_call__Tool
    tools.append(Awselb__custom_api_call__Tool())
    return tools
