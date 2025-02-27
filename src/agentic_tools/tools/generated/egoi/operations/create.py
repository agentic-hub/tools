from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EgoiCredentials

class EgoiCreateToolInput(BaseModel):
    list: Optional[str] = Field(None, description="ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resolve_data: Optional[bool] = Field(None, description="By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="Email address for a subscriber")
    contact_id: Optional[str] = Field(None, description="Contact ID of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class EgoiCreateTool(BaseTool):
    name: str = "egoi_create"
    description: str = "Tool for egoi create operation - create operation"
    args_schema: type[BaseModel] | None = EgoiCreateToolInput
    credentials: Optional[EgoiCredentials] = None
