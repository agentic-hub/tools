from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitLogToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitLogTool(BaseTool):
    name = "git_log"
    description = "Tool for git log operation - log operation"
    
    def _run(self, **kwargs):
        """Run the git log operation."""
        # Implement the tool logic here
        return f"Running git log operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git log operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
