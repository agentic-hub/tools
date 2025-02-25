from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class EmeliaAddToolInput(BaseModel):
    contactEmail: Optional[str] = Field(None, description="The email of the contact to add to the contact list")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    campaignId: Optional[str] = Field(None, description="The ID of the campaign to add the contact to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    campaignName: Optional[str] = Field(None, description="The name of the campaign to create")
    operation: Optional[str] = Field(None, description="Operation")
    contactListId: Optional[str] = Field(None, description="The ID of the contact list to add the contact to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")


class EmeliaAddTool(BaseTool):
    name = "emelia_add"
    description = "Tool for emelia add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the emelia add operation."""
        # Implement the tool logic here
        return f"Running emelia add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the emelia add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
