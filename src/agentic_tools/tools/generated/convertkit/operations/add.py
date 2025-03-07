from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ConvertkitCredentials

class ConvertkitAddToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    email: Optional[str] = Field(None, description="Subscriber email address")
    id: Optional[str] = Field(None, description="The ID of your custom field")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitAddTool(BaseTool):
    name: str = "convertkit_add"
    connector_id: str = "nodes-base.convertKit"
    description: str = "Tool for convertKit add operation - add operation"
    args_schema: type[BaseModel] | None = ConvertkitAddToolInput
    credentials: Optional[ConvertkitCredentials] = None
