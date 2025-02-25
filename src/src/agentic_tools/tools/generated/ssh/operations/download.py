from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SshDownloadToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Object property name which holds binary data")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The file path of the file to download. Has to contain the full path including file name.")


class SshDownloadTool(BaseTool):
    name = "ssh_download"
    description = "Tool for ssh download operation - download operation"
    
    def _run(self, **kwargs):
        """Run the ssh download operation."""
        # Implement the tool logic here
        return f"Running ssh download operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ssh download operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
