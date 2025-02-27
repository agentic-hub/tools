from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BoxCredentials

class BoxUploadToolInput(BaseModel):
    parent_id: Optional[str] = Field(None, description="ID of the parent folder that will contain the file. If not it will be uploaded to the root folder.")
    role: Optional[str] = Field(None, description="The level of access granted")
    file_id: Optional[str] = Field(None, description="File ID")
    user_id: Optional[str] = Field(None, description="The user's ID to share the file with")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    email: Optional[str] = Field(None, description="The user's email address to share the file with")
    file_content: Optional[str] = Field(None, description="The text content of the file")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    accessible_by: Optional[str] = Field(None, description="The type of object the file will be shared with")
    group_id: Optional[str] = Field(None, description="The group's ID to share the file with")
    query: Optional[str] = Field(None, description="The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    use_email: Optional[bool] = Field(None, description="Whether identify the user by email or ID")
    file_name: Optional[str] = Field(None, description="The name the file should be saved as")


class BoxUploadTool(BaseTool):
    name: str = "box_upload"
    description: str = "Tool for box upload operation - upload operation"
    args_schema: type[BaseModel] | None = BoxUploadToolInput
    credentials: Optional[BoxCredentials] = None
