from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ConvertkitCredentials

class ConvertkitGetsubscriptionsToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Receive only active subscribers or cancelled subscribers")
    email: Optional[str] = Field(None, description="The subscriber's email address")
    id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class ConvertkitGetsubscriptionsTool(BaseTool):
    name: str = "convertkit_getsubscriptions"
    connector_id: str = "nodes-base.convertKit"
    description: str = "Tool for convertKit getSubscriptions operation - getSubscriptions operation"
    args_schema: type[BaseModel] | None = ConvertkitGetsubscriptionsToolInput
    credentials: Optional[ConvertkitCredentials] = None
