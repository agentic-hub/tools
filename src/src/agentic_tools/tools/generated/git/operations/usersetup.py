from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitUsersetupToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitUsersetupTool(BaseTool):
    name = "git_usersetup"
    description = "Tool for git userSetup operation - userSetup operation"
    
    def _run(self, **kwargs):
        """Run the git userSetup operation."""
        # Implement the tool logic here
        return f"Running git userSetup operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git userSetup operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
