from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NextcloudMoveToolInput(BaseModel):
    toPath: Optional[str] = Field(None, description="The new path of file or folder. The path should start with \"/\".")
    path: Optional[str] = Field(None, description="The path of file or folder to move. The path should start with \"/\".")
    userId: Optional[str] = Field(None, description="Username the user will have")
    binaryPropertyName: Optional[str] = Field(None, description="Put Output File in Field")
    email: Optional[str] = Field(None, description="The Email address to share with")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")


class NextcloudMoveTool(BaseTool):
    name = "nextcloud_move"
    description = "Tool for nextCloud move operation - move operation"
    
    def _run(self, **kwargs):
        """Run the nextCloud move operation."""
        # Implement the tool logic here
        return f"Running nextCloud move operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the nextCloud move operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
