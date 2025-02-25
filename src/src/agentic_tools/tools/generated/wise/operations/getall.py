from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WiseGetallToolInput(BaseModel):
    quoteId: Optional[str] = Field(None, description="ID of the quote to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    transferId: Optional[str] = Field(None, description="ID of the transfer to delete")
    targetAccountId: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profileId: Optional[str] = Field(None, description="ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    fileName: Optional[str] = Field(None, description="Name of the file that will be downloaded")


class WiseGetallTool(BaseTool):
    name = "wise_getall"
    description = "Tool for wise getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the wise getAll operation."""
        # Implement the tool logic here
        return f"Running wise getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wise getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
