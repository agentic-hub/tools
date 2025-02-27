from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftonedriveCredentials

class MicrosoftonedriveRenameToolInput(BaseModel):
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")


class MicrosoftonedriveRenameTool(BaseTool):
    name: str = "microsoftonedrive_rename"
    connector_id: str = "nodes-base.microsoftOneDrive"
    description: str = "Tool for microsoftOneDrive rename operation - rename operation"
    args_schema: type[BaseModel] | None = MicrosoftonedriveRenameToolInput
    credentials: Optional[MicrosoftonedriveCredentials] = None
