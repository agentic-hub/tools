from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksGetToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="ID of user")
    resource: Optional[str] = Field(None, description="Resource")
    my_library: Optional[bool] = Field(None, description="My Library")
    volume_id: Optional[str] = Field(None, description="ID of the volume")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksGetTool(BaseTool):
    name: str = "googlebooks_get"
    connector_id: str = "nodes-base.googleBooks"
    description: str = "Tool for googleBooks get operation - get operation"
    args_schema: type[BaseModel] | None = GooglebooksGetToolInput
    credentials: Optional[GooglebooksCredentials] = None
