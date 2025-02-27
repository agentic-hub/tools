from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksRemoveToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    volume_id: Optional[str] = Field(None, description="ID of the volume")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksRemoveTool(BaseTool):
    name: str = "googlebooks_remove"
    connector_id: str = "nodes-base.googleBooks"
    description: str = "Tool for googleBooks remove operation - remove operation"
    args_schema: type[BaseModel] | None = GooglebooksRemoveToolInput
    credentials: Optional[GooglebooksCredentials] = None
