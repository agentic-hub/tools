from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglebooksCredentials

class GooglebooksGetallToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="ID of user")
    resource: Optional[str] = Field(None, description="Resource")
    my_library: Optional[bool] = Field(None, description="My Library")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    search_query: Optional[str] = Field(None, description="Full-text search query string")
    authentication: Optional[str] = Field(None, description="Authentication")
    shelf_id: Optional[str] = Field(None, description="ID of the bookshelf")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebooksGetallTool(BaseTool):
    name: str = "googlebooks_getall"
    connector_id: str = "nodes-base.googleBooks"
    description: str = "Tool for googleBooks getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GooglebooksGetallToolInput
    credentials: Optional[GooglebooksCredentials] = None
