from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecontactsCredentials

class GooglecontactsUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsUpdateTool(BaseTool):
    name: str = "googlecontacts_update"
    connector_id: str = "nodes-base.googleContacts"
    description: str = "Tool for googleContacts update operation - update operation"
    args_schema: type[BaseModel] | None = GooglecontactsUpdateToolInput
    credentials: Optional[GooglecontactsCredentials] = None
