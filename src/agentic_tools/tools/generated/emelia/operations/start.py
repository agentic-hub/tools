from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmeliaStartToolInput(BaseModel):
    contactEmail: Optional[str] = Field(None, description="The email of the contact to add to the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[str] = Field(None, description="The ID of the campaign to start. Email provider and contacts must be set.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaignName: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")


class EmeliaStartTool(BaseTool):
    name = "emelia_start"
    description = "Tool for emelia start operation - start operation"
    
    def _run(self, **kwargs):
        """Run the emelia start operation."""
        # Implement the tool logic here
        return f"Running emelia start operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emelia start operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
