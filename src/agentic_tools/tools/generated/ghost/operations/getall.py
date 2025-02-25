from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GhostGetallToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    postId: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    contentFormat: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostGetallTool(BaseTool):
    name = "ghost_getall"
    description = "Tool for ghost getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the ghost getAll operation."""
        # Implement the tool logic here
        return f"Running ghost getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the ghost getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
