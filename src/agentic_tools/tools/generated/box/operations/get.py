from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BoxGetToolInput(BaseModel):
    parentId: Optional[str] = Field(None, description="The ID of folder to copy the file to. If not defined will be copied to the root folder.")
    role: Optional[str] = Field(None, description="The level of access granted")
    fileId: Optional[str] = Field(None, description="Field ID")
    userId: Optional[str] = Field(None, description="The user's ID to share the file with")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The user's email address to share the file with")
    folderId: Optional[str] = Field(None, description="Folder ID")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    accessibleBy: Optional[str] = Field(None, description="The type of object the file will be shared with")
    groupId: Optional[str] = Field(None, description="The group's ID to share the file with")
    query: Optional[str] = Field(None, description="The string to search for. This query is matched against item names, descriptions, text content of files, and various other fields of the different item types.")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    useEmail: Optional[bool] = Field(None, description="Whether identify the user by email or ID")


class BoxGetTool(BaseTool):
    name = "box_get"
    description = "Tool for box get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the box get operation."""
        # Implement the tool logic here
        return f"Running box get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the box get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
