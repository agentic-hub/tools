from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import EgoiCredentials

class EgoiUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    list: Optional[str] = Field(None, description="ID of list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resolve_data: Optional[bool] = Field(None, description="By default the response just includes the contact ID. If this option gets activated, it will resolve the data automatically.")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="Email address for a subscriber")
    contact_id: Optional[str] = Field(None, description="Contact ID of the subscriber")
    operation: Optional[str] = Field(None, description="Operation")


class EgoiUpdateTool(BaseTool):
    name: str = "egoi_update"
    connector_id: str = "nodes-base.egoi"
    description: str = "Tool for egoi update operation - update operation"
    args_schema: type[BaseModel] | None = EgoiUpdateToolInput
    credentials: Optional[EgoiCredentials] = None
