from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CircleciGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    projectSlug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciGetallTool(BaseTool):
    name = "circleci_getall"
    description = "Tool for circleCi getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the circleCi getAll operation."""
        # Implement the tool logic here
        return f"Running circleCi getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the circleCi getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
