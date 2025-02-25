from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CircleciTriggerToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    projectSlug: Optional[str] = Field(None, description="Project slug in the form org-name/repo-name")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    vcs: Optional[str] = Field(None, description="Source control system")
    operation: Optional[str] = Field(None, description="Operation")


class CircleciTriggerTool(BaseTool):
    name = "circleci_trigger"
    description = "Tool for circleCi trigger operation - trigger operation"
    
    def _run(self, **kwargs):
        """Run the circleCi trigger operation."""
        # Implement the tool logic here
        return f"Running circleCi trigger operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the circleCi trigger operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
