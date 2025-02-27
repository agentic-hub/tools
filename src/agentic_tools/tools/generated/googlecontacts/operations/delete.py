from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecontactsCredentials

class GooglecontactsDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsDeleteTool(BaseTool):
    name: str = "googlecontacts_delete"
    connector_id: str = "nodes-base.googleContacts"
    description: str = "Tool for googleContacts delete operation - delete operation"
    args_schema: type[BaseModel] | None = GooglecontactsDeleteToolInput
    credentials: Optional[GooglecontactsCredentials] = None
