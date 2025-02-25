from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NextcloudShareToolInput(BaseModel):
    toPath: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The file path of the file to share. Has to contain the full path. The path should start with \"/\".")
    userId: Optional[str] = Field(None, description="Username the user will have")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    shareType: Optional[str] = Field(None, description="The share permissions to set")
    circleId: Optional[str] = Field(None, description="The ID of the circle to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    groupId: Optional[str] = Field(None, description="The ID of the group to share with")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[str] = Field(None, description="The user to share with")


class NextcloudShareTool(BaseTool):
    name = "nextcloud_share"
    description = "Tool for nextCloud share operation - share operation"
    
    def _run(self, **kwargs):
        """Run the nextCloud share operation."""
        # Implement the tool logic here
        return f"Running nextCloud share operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nextCloud share operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
