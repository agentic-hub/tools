from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssesCredentials

class AwssesDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    to_addresses: Optional[str] = Field(None, description="Email addresses of the recipients")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    from_email: Optional[str] = Field(None, description="Email address of the sender")
    template_name: Optional[str] = Field(None, description="The name of the custom verification email template")


class AwssesDeleteTool(BaseTool):
    name: str = "awsses_delete"
    description: str = "Tool for awsSes delete operation - delete operation"
    args_schema: type[BaseModel] | None = AwssesDeleteToolInput
    credentials: Optional[AwssesCredentials] = None
