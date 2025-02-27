from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksAddToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    volume_id: Optional[str] = Field(None, description="ID of the volume")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksAddTool(BaseTool):
    name: str = "googlebooks_add"
    description: str = "Tool for googleBooks add operation - add operation"
    args_schema: type[BaseModel] | None = GooglebooksAddToolInput
    credentials: Optional[GooglebooksCredentials] = None
