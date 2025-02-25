from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SshUploadToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter \"File Name\" under options.")


class SshUploadTool(BaseTool):
    name = "ssh_upload"
    description = "Tool for ssh upload operation - upload operation"
    
    def _run(self, **kwargs):
        """Run the ssh upload operation."""
        # Implement the tool logic here
        return f"Running ssh upload operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ssh upload operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
