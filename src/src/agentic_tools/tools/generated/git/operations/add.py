from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitAddToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    pathsToAdd: Optional[str] = Field(None, description="Comma-separated list of paths (absolute or relative to Repository Path) of files or folders to add")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitAddTool(BaseTool):
    name = "git_add"
    description = "Tool for git add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the git add operation."""
        # Implement the tool logic here
        return f"Running git add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
