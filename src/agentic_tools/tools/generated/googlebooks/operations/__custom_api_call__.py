from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class Googlebooks__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class Googlebooks__custom_api_call__Tool(BaseTool):
    name: str = "googlebooks___custom_api_call__"
    connector_id: str = "nodes-base.googleBooks"
    description: str = "Tool for googleBooks __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googlebooks__custom_api_call__ToolInput
    credentials: Optional[GooglebooksCredentials] = None
