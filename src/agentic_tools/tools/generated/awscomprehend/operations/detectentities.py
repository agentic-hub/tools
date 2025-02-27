from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwscomprehendCredentials

class AwscomprehendDetectentitiesToolInput(BaseModel):
    language_code: Optional[str] = Field(None, description="The language code for text")
    resource: Optional[str] = Field(None, description="The resource to perform")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    text: Optional[str] = Field(None, description="The text to send")
    operation: Optional[str] = Field(None, description="Operation")


class AwscomprehendDetectentitiesTool(BaseTool):
    name: str = "awscomprehend_detectentities"
    connector_id: str = "nodes-base.awsComprehend"
    description: str = "Tool for awsComprehend detectEntities operation - detectEntities operation"
    args_schema: type[BaseModel] | None = AwscomprehendDetectentitiesToolInput
    credentials: Optional[AwscomprehendCredentials] = None
