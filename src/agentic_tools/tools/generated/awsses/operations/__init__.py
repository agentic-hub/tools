# awsSes operations
from typing import List
from langchain.tools import BaseTool
from .. import AwssesCredentials

def get_tools() -> List[BaseTool]:
    """Get all awsSes operation tools."""
    tools = []
    from .create import AwssesCreateTool
    tools.append(AwssesCreateTool())
    from .delete import AwssesDeleteTool
    tools.append(AwssesDeleteTool())
    from .get import AwssesGetTool
    tools.append(AwssesGetTool())
    from .getall import AwssesGetallTool
    tools.append(AwssesGetallTool())
    from .send import AwssesSendTool
    tools.append(AwssesSendTool())
    from .update import AwssesUpdateTool
    tools.append(AwssesUpdateTool())
    from .__custom_api_call__ import Awsses__custom_api_call__Tool
    tools.append(Awsses__custom_api_call__Tool())
    from .send import AwssesSendTool
    tools.append(AwssesSendTool())
    from .sendtemplate import AwssesSendtemplateTool
    tools.append(AwssesSendtemplateTool())
    from .__custom_api_call__ import Awsses__custom_api_call__Tool
    tools.append(Awsses__custom_api_call__Tool())
    from .create import AwssesCreateTool
    tools.append(AwssesCreateTool())
    from .delete import AwssesDeleteTool
    tools.append(AwssesDeleteTool())
    from .get import AwssesGetTool
    tools.append(AwssesGetTool())
    from .getall import AwssesGetallTool
    tools.append(AwssesGetallTool())
    from .update import AwssesUpdateTool
    tools.append(AwssesUpdateTool())
    from .__custom_api_call__ import Awsses__custom_api_call__Tool
    tools.append(Awsses__custom_api_call__Tool())
    return tools
