from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftonedriveDeleteToolInput(BaseModel):
    fileId: Optional[str] = Field(None, description="Field ID")
    type: Optional[str] = Field(None, description="The type of sharing link to create")
    itemId: Optional[str] = Field(None, description="ID of the file")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    folderId: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    scope: Optional[str] = Field(None, description="The type of sharing link to create")
    query: Optional[str] = Field(None, description="The query text used to search for items. Values may be matched across several fields including filename, metadata, and file content.")
    resource: Optional[str] = Field(None, description="Resource")
    newName: Optional[str] = Field(None, description="New name for file")


class MicrosoftonedriveDeleteTool(BaseTool):
    name = "microsoftonedrive_delete"
    description = "Tool for microsoftOneDrive delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the microsoftOneDrive delete operation."""
        # Implement the tool logic here
        return f"Running microsoftOneDrive delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftOneDrive delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
