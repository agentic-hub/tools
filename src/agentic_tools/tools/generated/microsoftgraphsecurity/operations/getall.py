from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftgraphsecurityGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    secureScoreControlProfileId: Optional[str] = Field(None, description="ID of the secure score control profile to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftgraphsecurityGetallTool(BaseTool):
    name = "microsoftgraphsecurity_getall"
    description = "Tool for microsoftGraphSecurity getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the microsoftGraphSecurity getAll operation."""
        # Implement the tool logic here
        return f"Running microsoftGraphSecurity getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftGraphSecurity getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
