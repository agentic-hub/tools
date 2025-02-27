from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssesCredentials

class AwssesCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    html_part: Optional[str] = Field(None, description="The HTML body of the email")
    template_subject: Optional[str] = Field(None, description="The subject line of the custom verification email")
    failure_redirection_url: Optional[str] = Field(None, description="The URL that the recipient of the verification email is sent to if his or her address is not successfully verified")
    subject_part: Optional[str] = Field(None, description="The subject line of the email")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    success_redirection_url: Optional[str] = Field(None, description="The URL that the recipient of the verification email is sent to if his or her address is successfully verified")
    from_email_address: Optional[str] = Field(None, description="The email address that the custom verification email is sent from")
    template_content: Optional[str] = Field(None, description="The content of the custom verification email. The total size of the email must be less than 10 MB. The message body may contain HTML")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The name of the custom verification email template")


class AwssesCreateTool(BaseTool):
    name: str = "awsses_create"
    description: str = "Tool for awsSes create operation - create operation"
    args_schema: type[BaseModel] | None = AwssesCreateToolInput
    credentials: Optional[AwssesCredentials] = None
