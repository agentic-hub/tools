from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitAddconfigToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    value: Optional[str] = Field(None, description="Value of the key to set")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    key: Optional[str] = Field(None, description="Name of the key to set")
    operation: Optional[str] = Field(None, description="Operation")


class GitAddconfigTool(BaseTool):
    name = "git_addconfig"
    description = "Tool for git addConfig operation - addConfig operation"
    
    def _run(self, **kwargs):
        """Run the git addConfig operation."""
        # Implement the tool logic here
        return f"Running git addConfig operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git addConfig operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
