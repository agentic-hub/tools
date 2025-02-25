from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DisqusGetToolInput(BaseModel):
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The short name(aka ID) of the forum to get")
    operation: Optional[str] = Field(None, description="Operation")


class DisqusGetTool(BaseTool):
    name = "disqus_get"
    description = "Tool for disqus get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the disqus get operation."""
        # Implement the tool logic here
        return f"Running disqus get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the disqus get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
