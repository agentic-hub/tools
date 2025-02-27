from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftonedriveCredentials

class MicrosoftonedriveCopyToolInput(BaseModel):
    parent_reference: Optional[Dict[str, Any]] = Field(None, description="Reference to the parent item the copy will be created in <a href=\"https://docs.microsoft.com/en-us/onedrive/developer/rest-api/resources/itemreference?view=odsp-graph-online\"> Details </a>")
    file_id: Optional[str] = Field(None, description="File ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    item_id: Optional[str] = Field(None, description="ID of the file")
    binary_property_name: Optional[str] = Field(None, description="Put Output File in Field")
    folder_id: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    new_name: Optional[str] = Field(None, description="New name for file")


class MicrosoftonedriveCopyTool(BaseTool):
    name: str = "microsoftonedrive_copy"
    connector_id: str = "nodes-base.microsoftOneDrive"
    description: str = "Tool for microsoftOneDrive copy operation - copy operation"
    args_schema: type[BaseModel] | None = MicrosoftonedriveCopyToolInput
    credentials: Optional[MicrosoftonedriveCredentials] = None
