from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftgraphsecurityGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    secureScoreId: Optional[str] = Field(None, description="ID of the secure score to retrieve")
    secureScoreControlProfileId: Optional[str] = Field(None, description="ID of the secure score control profile to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftgraphsecurityGetTool(BaseTool):
    name = "microsoftgraphsecurity_get"
    description = "Tool for microsoftGraphSecurity get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the microsoftGraphSecurity get operation."""
        # Implement the tool logic here
        return f"Running microsoftGraphSecurity get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftGraphSecurity get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
