from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CircleciGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    pipelineNumber: Optional[float] = Field(None, description="The number of the pipeline")
    projectSlug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciGetTool(BaseTool):
    name = "circleci_get"
    description = "Tool for circleCi get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the circleCi get operation."""
        # Implement the tool logic here
        return f"Running circleCi get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the circleCi get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
