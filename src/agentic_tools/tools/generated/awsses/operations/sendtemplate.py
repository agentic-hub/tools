from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssesCredentials

class AwssesSendtemplateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    template_data_ui: Optional[Dict[str, Any]] = Field(None, description="Template Data")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The ARN of the template to use when sending this email. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class AwssesSendtemplateTool(BaseTool):
    name: str = "awsses_sendtemplate"
    description: str = "Tool for awsSes sendTemplate operation - sendTemplate operation"
    args_schema: type[BaseModel] | None = AwssesSendtemplateToolInput
    credentials: Optional[AwssesCredentials] = None
