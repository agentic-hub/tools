from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitPullToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitPullTool(BaseTool):
    name = "git_pull"
    description = "Tool for git pull operation - pull operation"
    
    def _run(self, **kwargs):
        """Run the git pull operation."""
        # Implement the tool logic here
        return f"Running git pull operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git pull operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
