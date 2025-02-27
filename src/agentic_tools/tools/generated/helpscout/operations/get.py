from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HelpscoutCredentials

class HelpscoutGetToolInput(BaseModel):
    mailbox_id: Optional[str] = Field(None, description="Mailbox ID")
    customer_id: Optional[str] = Field(None, description="Customer ID")
    type: Optional[str] = Field(None, description="Conversation type")
    resolve_data: Optional[bool] = Field(None, description="By default the response only contain the ID to resource. If this option gets activated, it will resolve the data automatically.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="Conversation ID")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class HelpscoutGetTool(BaseTool):
    name: str = "helpscout_get"
    description: str = "Tool for helpScout get operation - get operation"
    args_schema: type[BaseModel] | None = HelpscoutGetToolInput
    credentials: Optional[HelpscoutCredentials] = None
