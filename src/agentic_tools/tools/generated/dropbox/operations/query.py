from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DropboxCredentials

class DropboxQueryToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    to_path: Optional[str] = Field(None, description="The destination path of file or folder")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Means of authenticating with the service")
    file_status: Optional[str] = Field(None, description="The string to search for. May match across multiple fields based on the request arguments.")
    query: Optional[str] = Field(None, description="The string to search for. May match across multiple fields based on the request arguments.")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The path of file or folder to copy")


class DropboxQueryTool(BaseTool):
    name: str = "dropbox_query"
    description: str = "Tool for dropbox query operation - query operation"
    args_schema: type[BaseModel] | None = DropboxQueryToolInput
    credentials: Optional[DropboxCredentials] = None
