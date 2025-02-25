from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GitlabtriggerDefaultToolInput(BaseModel):
    repository: Optional[str] = Field(None, description="The name of the repsitory")
    authentication: Optional[str] = Field(None, description="Authentication")
    events: Optional[str] = Field(None, description="events")
    owner: Optional[str] = Field(None, description="Owner of the repsitory")


class GitlabtriggerDefaultTool(BaseTool):
    name = "gitlabtrigger_default"
    description = "Tool for gitlabTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the gitlabTrigger default operation."""
        # Implement the tool logic here
        return f"Running gitlabTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the gitlabTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
