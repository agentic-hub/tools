from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TravisciGetallToolInput(BaseModel):
    buildId: Optional[str] = Field(None, description="Value uniquely identifying the build")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class TravisciGetallTool(BaseTool):
    name = "travisci_getall"
    description = "Tool for travisCi getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the travisCi getAll operation."""
        # Implement the tool logic here
        return f"Running travisCi getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the travisCi getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
