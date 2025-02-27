from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DropboxCredentials

class DropboxListToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    to_path: Optional[str] = Field(None, description="The destination path of file or folder")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Means of authenticating with the service")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The path of which to list the content")


class DropboxListTool(BaseTool):
    name: str = "dropbox_list"
    connector_id: str = "nodes-base.dropbox"
    description: str = "Tool for dropbox list operation - list operation"
    args_schema: type[BaseModel] | None = DropboxListToolInput
    credentials: Optional[DropboxCredentials] = None
