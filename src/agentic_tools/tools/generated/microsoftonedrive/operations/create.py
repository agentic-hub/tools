from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftonedriveCredentials

class MicrosoftonedriveCreateToolInput(BaseModel):
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name or path of the folder")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")


class MicrosoftonedriveCreateTool(BaseTool):
    name: str = "microsoftonedrive_create"
    connector_id: str = "nodes-base.microsoftOneDrive"
    description: str = "Tool for microsoftOneDrive create operation - create operation"
    args_schema: type[BaseModel] | None = MicrosoftonedriveCreateToolInput
    credentials: Optional[MicrosoftonedriveCredentials] = None
