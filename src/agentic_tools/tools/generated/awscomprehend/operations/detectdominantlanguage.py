from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscomprehendCredentials

class AwscomprehendDetectdominantlanguageToolInput(BaseModel):
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="The resource to perform")
    text: Optional[str] = Field(None, description="The text to send")
    operation: Optional[str] = Field(None, description="Operation")


class AwscomprehendDetectdominantlanguageTool(BaseTool):
    name: str = "awscomprehend_detectdominantlanguage"
    connector_id: str = "nodes-base.awsComprehend"
    description: str = "Tool for awsComprehend detectDominantLanguage operation - detectDominantLanguage operation"
    args_schema: type[BaseModel] | None = AwscomprehendDetectdominantlanguageToolInput
    credentials: Optional[AwscomprehendCredentials] = None
