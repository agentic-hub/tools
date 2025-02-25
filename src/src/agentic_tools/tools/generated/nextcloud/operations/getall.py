from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NextcloudGetallToolInput(BaseModel):
    toPath: Optional[str] = Field(None, description="The destination path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The path of file or folder to copy. The path should start with \"/\".")
    userId: Optional[str] = Field(None, description="Username the user will have")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudGetallTool(BaseTool):
    name = "nextcloud_getall"
    description = "Tool for nextCloud getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the nextCloud getAll operation."""
        # Implement the tool logic here
        return f"Running nextCloud getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nextCloud getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
