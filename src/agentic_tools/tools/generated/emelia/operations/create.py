from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmeliaCreateToolInput(BaseModel):
    contactEmail: Optional[str] = Field(None, description="The email of the contact to add to the campaign")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[str] = Field(None, description="The ID of the campaign to add the contact to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaignName: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")


class EmeliaCreateTool(BaseTool):
    name = "emelia_create"
    description = "Tool for emelia create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the emelia create operation."""
        # Implement the tool logic here
        return f"Running emelia create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emelia create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
