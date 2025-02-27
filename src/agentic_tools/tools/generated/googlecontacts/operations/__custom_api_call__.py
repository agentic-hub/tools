from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecontactsCredentials

class Googlecontacts__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    raw_data: Optional[bool] = Field(None, description="Whether to return the data exactly in the way it got received from the API")
    fields: Optional[str] = Field(None, description="fields")
    operation: Optional[str] = Field(None, description="Operation")


class Googlecontacts__custom_api_call__Tool(BaseTool):
    name: str = "googlecontacts___custom_api_call__"
    connector_id: str = "nodes-base.googleContacts"
    description: str = "Tool for googleContacts __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlecontacts__custom_api_call__ToolInput
    credentials: Optional[GooglecontactsCredentials] = None
