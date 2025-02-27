from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DropboxCredentials

class DropboxUploadToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    to_path: Optional[str] = Field(None, description="The destination path of file or folder")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Means of authenticating with the service")
    file_content: Optional[str] = Field(None, description="The text content of the file to upload")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to upload. Has to contain the full path. The parent folder has to exist. Existing files get overwritten.")


class DropboxUploadTool(BaseTool):
    name: str = "dropbox_upload"
    description: str = "Tool for dropbox upload operation - upload operation"
    args_schema: type[BaseModel] | None = DropboxUploadToolInput
    credentials: Optional[DropboxCredentials] = None
