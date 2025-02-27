from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ConvertkitCredentials

class ConvertkitGetallToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Receive only active subscribers or cancelled subscribers")
    tag_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="The ID of your custom field")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitGetallTool(BaseTool):
    name: str = "convertkit_getall"
    connector_id: str = "nodes-base.convertKit"
    description: str = "Tool for convertKit getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ConvertkitGetallToolInput
    credentials: Optional[ConvertkitCredentials] = None
