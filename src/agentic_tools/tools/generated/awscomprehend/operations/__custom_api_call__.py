from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscomprehendCredentials

class Awscomprehend__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="The resource to perform")
    text: Optional[str] = Field(None, description="The text to send")
    operation: Optional[str] = Field(None, description="Operation")


class Awscomprehend__custom_api_call__Tool(BaseTool):
    name: str = "awscomprehend___custom_api_call__"
    description: str = "Tool for awsComprehend __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awscomprehend__custom_api_call__ToolInput
    credentials: Optional[AwscomprehendCredentials] = None
