from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NextcloudDeleteToolInput(BaseModel):
    toPath: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The path to delete. Can be a single file or a whole folder. The path should start with \"/\".")
    userId: Optional[str] = Field(None, description="Username the user will have")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudDeleteTool(BaseTool):
    name = "nextcloud_delete"
    description = "Tool for nextCloud delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the nextCloud delete operation."""
        # Implement the tool logic here
        return f"Running nextCloud delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nextCloud delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
