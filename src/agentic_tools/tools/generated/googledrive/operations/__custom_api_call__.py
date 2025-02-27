from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogledriveCredentials

class Googledrive__custom_api_call__ToolInput(BaseModel):
    query_string: Optional[str] = Field(None, description="The name of the file or folder to search for. Returns also files and folders whose names partially match this search term.")
    file_id: Optional[Dict[str, Any]] = Field(None, description="The file to copy")
    input_data_field_name: Optional[str] = Field(None, description="Find the name of input field containing the binary data to update the file in the Input panel on the left, in the Binary tab")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    drive_id: Optional[Dict[str, Any]] = Field(None, description="The shared drive to delete")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="The folder where to save the copied file")
    operation: Optional[str] = Field(None, description="Operation")
    permissions_ui: Optional[Dict[str, Any]] = Field(None, description="Permissions")
    name: Optional[str] = Field(None, description="The name of the shared drive to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    folder_no_root_id: Optional[Dict[str, Any]] = Field(None, description="The folder to delete")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class Googledrive__custom_api_call__Tool(BaseTool):
    name: str = "googledrive___custom_api_call__"
    description: str = "Tool for googleDrive __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Googledrive__custom_api_call__ToolInput
    credentials: Optional[GoogledriveCredentials] = None
