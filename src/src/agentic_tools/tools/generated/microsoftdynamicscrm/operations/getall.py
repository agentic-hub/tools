from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftdynamicscrmGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftdynamicscrmGetallTool(BaseTool):
    name = "microsoftdynamicscrm_getall"
    description = "Tool for microsoftDynamicsCrm getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the microsoftDynamicsCrm getAll operation."""
        # Implement the tool logic here
        return f"Running microsoftDynamicsCrm getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftDynamicsCrm getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
