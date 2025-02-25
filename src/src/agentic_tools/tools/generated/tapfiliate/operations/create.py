from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class TapfiliateCreateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    lastname: Optional[str] = Field(None, description="The affiliate’s lastname")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The affiliate’s email")
    programId: Optional[str] = Field(None, description="The ID of the Program to add the affiliate to. This ID can be found as part of the URL when viewing the program on the platform. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    key: Optional[str] = Field(None, description="Name of the metadata key to remove")
    affiliateId: Optional[str] = Field(None, description="The ID of the affiliate")
    firstname: Optional[str] = Field(None, description="The affiliate’s firstname")
    operation: Optional[str] = Field(None, description="Operation")


class TapfiliateCreateTool(BaseTool):
    name = "tapfiliate_create"
    description = "Tool for tapfiliate create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the tapfiliate create operation."""
        # Implement the tool logic here
        return f"Running tapfiliate create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the tapfiliate create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
