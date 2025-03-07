from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledriveCredentials

class GoogledriveUpdateToolInput(BaseModel):
    query_string: Optional[str] = Field(None, description="The name of the file or folder to search for. Returns also files and folders whose names partially match this search term.")
    change_file_content: Optional[bool] = Field(None, description="Whether to send a new binary data to update the file")
    file_id: Optional[Dict[str, Any]] = Field(None, description="The file to update")
    input_data_field_name: Optional[str] = Field(None, description="Find the name of input field containing the binary data to update the file in the Input panel on the left, in the Binary tab")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    drive_id: Optional[Dict[str, Any]] = Field(None, description="The shared drive to update")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="The folder where to save the copied file")
    operation: Optional[str] = Field(None, description="Operation")
    permissions_ui: Optional[Dict[str, Any]] = Field(None, description="Permissions")
    name: Optional[str] = Field(None, description="The name of the shared drive to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    folder_no_root_id: Optional[Dict[str, Any]] = Field(None, description="The folder to delete")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    new_updated_file_name: Optional[str] = Field(None, description="If not specified, the file name will not be changed")


class GoogledriveUpdateTool(BaseTool):
    name: str = "googledrive_update"
    connector_id: str = "nodes-base.googleDrive"
    description: str = "Tool for googleDrive update operation - update operation"
    args_schema: type[BaseModel] | None = GoogledriveUpdateToolInput
    credentials: Optional[GoogledriveCredentials] = None
