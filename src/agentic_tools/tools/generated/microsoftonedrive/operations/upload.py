from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftonedriveCredentials

class MicrosoftonedriveUploadToolInput(BaseModel):
    parent_id: Optional[str] = Field(None, description="ID of the parent folder that will contain the file")
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Input Binary Field")
    file_content: Optional[str] = Field(None, description="The text content of the file")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    binary_data: Optional[bool] = Field(None, description="Whether the data to upload should be taken from binary field")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")
    file_name: Optional[str] = Field(None, description="The name the file should be saved as")


class MicrosoftonedriveUploadTool(BaseTool):
    name: str = "microsoftonedrive_upload"
    connector_id: str = "nodes-base.microsoftOneDrive"
    description: str = "Tool for microsoftOneDrive upload operation - upload operation"
    args_schema: type[BaseModel] | None = MicrosoftonedriveUploadToolInput
    credentials: Optional[MicrosoftonedriveCredentials] = None
