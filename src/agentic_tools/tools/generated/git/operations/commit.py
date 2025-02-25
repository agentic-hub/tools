from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitCommitToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="The commit message to use")
    operation: Optional[str] = Field(None, description="Operation")


class GitCommitTool(BaseTool):
    name = "git_commit"
    description = "Tool for git commit operation - commit operation"
    
    def _run(self, **kwargs):
        """Run the git commit operation."""
        # Implement the tool logic here
        return f"Running git commit operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git commit operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
