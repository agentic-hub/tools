from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SshExecuteToolInput(BaseModel):
    cwd: Optional[str] = Field(None, description="Working Directory")
    resource: Optional[str] = Field(None, description="Resource")
    binaryPropertyName: Optional[str] = Field(None, description="Input Binary Field")
    authentication: Optional[str] = Field(None, description="Authentication")
    command: Optional[str] = Field(None, description="The command to be executed on a remote device")
    operation: Optional[str] = Field(None, description="Operation")
    path: Optional[str] = Field(None, description="The directory to upload the file to. The name of the file does not need to be specified, it's taken from the binary data file name. To override this behavior, set the parameter \"File Name\" under options.")


class SshExecuteTool(BaseTool):
    name = "ssh_execute"
    description = "Tool for ssh execute operation - execute operation"
    
    def _run(self, **kwargs):
        """Run the ssh execute operation."""
        # Implement the tool logic here
        return f"Running ssh execute operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ssh execute operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
