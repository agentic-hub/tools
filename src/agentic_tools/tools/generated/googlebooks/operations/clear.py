from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksClearToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksClearTool(BaseTool):
    name: str = "googlebooks_clear"
    description: str = "Tool for googleBooks clear operation - clear operation"
    args_schema: type[BaseModel] | None = GooglebooksClearToolInput
    credentials: Optional[GooglebooksCredentials] = None
