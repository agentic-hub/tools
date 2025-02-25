from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitListconfigToolInput(BaseModel):
    repositoryPath: Optional[str] = Field(None, description="Local path of the git repository to operate on")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GitListconfigTool(BaseTool):
    name = "git_listconfig"
    description = "Tool for git listConfig operation - listConfig operation"
    
    def _run(self, **kwargs):
        """Run the git listConfig operation."""
        # Implement the tool logic here
        return f"Running git listConfig operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the git listConfig operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
