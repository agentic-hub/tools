from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledriveCredentials

class GoogledriveUploadToolInput(BaseModel):
    query_string: Optional[str] = Field(None, description="The name of the file or folder to search for. Returns also files and folders whose names partially match this search term.")
    file_id: Optional[Dict[str, Any]] = Field(None, description="The file to copy")
    input_data_field_name: Optional[str] = Field(None, description="Find the name of input field containing the binary data to update the file in the Input panel on the left, in the Binary tab")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    drive_id: Optional[Dict[str, Any]] = Field(None, description="The drive where to upload the file")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="The folder where to upload the file")
    operation: Optional[str] = Field(None, description="Operation")
    permissions_ui: Optional[Dict[str, Any]] = Field(None, description="Permissions")
    name: Optional[str] = Field(None, description="If not specified, the original file name will be used")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    folder_no_root_id: Optional[Dict[str, Any]] = Field(None, description="The folder to delete")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class GoogledriveUploadTool(BaseTool):
    name: str = "googledrive_upload"
    connector_id: str = "nodes-base.googleDrive"
    description: str = "Tool for googleDrive upload operation - upload operation"
    args_schema: type[BaseModel] | None = GoogledriveUploadToolInput
    credentials: Optional[GoogledriveCredentials] = None
