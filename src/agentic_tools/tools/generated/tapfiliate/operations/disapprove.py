from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TapfiliateDisapproveToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    programId: Optional[str] = Field(None, description="The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    key: Optional[str] = Field(None, description="Name of the metadata key to remove")
    affiliateId: Optional[str] = Field(None, description="The ID of the affiliate")
    operation: Optional[str] = Field(None, description="Operation")


class TapfiliateDisapproveTool(BaseTool):
    name = "tapfiliate_disapprove"
    description = "Tool for tapfiliate disapprove operation - disapprove operation"
    
    def _run(self, **kwargs):
        """Run the tapfiliate disapprove operation."""
        # Implement the tool logic here
        return f"Running tapfiliate disapprove operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the tapfiliate disapprove operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
