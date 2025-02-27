from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssesCredentials

class AwssesSendToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    is_body_html: Optional[bool] = Field(None, description="Whether body is HTML or simple text")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The email address to verify")
    subject: Optional[str] = Field(None, description="Subject")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    body: Optional[str] = Field(None, description="The message to be sent")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The name of the custom verification email template to use when sending the verification email")


class AwssesSendTool(BaseTool):
    name: str = "awsses_send"
    description: str = "Tool for awsSes send operation - send operation"
    args_schema: type[BaseModel] | None = AwssesSendToolInput
    credentials: Optional[AwssesCredentials] = None
