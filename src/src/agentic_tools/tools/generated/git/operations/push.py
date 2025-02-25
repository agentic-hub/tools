from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitPushToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="The way to authenticate")
    operation: Optional[str] = Field(None, description="Operation")


class GitPushTool(BaseTool):
    name = "git_push"
    description = "Tool for git push operation - push operation"
    
    def _run(self, **kwargs):
        """Run the git push operation."""
        # Implement the tool logic here
        return f"Running git push operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git push operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
