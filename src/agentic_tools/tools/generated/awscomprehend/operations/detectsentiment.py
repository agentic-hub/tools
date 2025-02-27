from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscomprehendCredentials

class AwscomprehendDetectsentimentToolInput(BaseModel):
    language_code: Optional[str] = Field(None, description="The language code for text")
    resource: Optional[str] = Field(None, description="The resource to perform")
    text: Optional[str] = Field(None, description="The text to send")
    operation: Optional[str] = Field(None, description="Operation")


class AwscomprehendDetectsentimentTool(BaseTool):
    name: str = "awscomprehend_detectsentiment"
    connector_id: str = "nodes-base.awsComprehend"
    description: str = "Tool for awsComprehend detectSentiment operation - detectSentiment operation"
    args_schema: type[BaseModel] | None = AwscomprehendDetectsentimentToolInput
    credentials: Optional[AwscomprehendCredentials] = None
