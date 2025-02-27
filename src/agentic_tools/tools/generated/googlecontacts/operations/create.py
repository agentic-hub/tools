from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecontactsCredentials

class GooglecontactsCreateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    given_name: Optional[str] = Field(None, description="Given Name")
    family_name: Optional[str] = Field(None, description="Family Name")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecontactsCreateTool(BaseTool):
    name: str = "googlecontacts_create"
    connector_id: str = "nodes-base.googleContacts"
    description: str = "Tool for googleContacts create operation - create operation"
    args_schema: type[BaseModel] | None = GooglecontactsCreateToolInput
    credentials: Optional[GooglecontactsCredentials] = None
