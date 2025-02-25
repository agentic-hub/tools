from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WiseGetstatementToolInput(BaseModel):
    format: Optional[str] = Field(None, description="File format to retrieve the statement in")
    quoteId: Optional[str] = Field(None, description="ID of the quote to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    borderlessAccountId: Optional[str] = Field(None, description="ID of the borderless account to retrieve the statement of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    transferId: Optional[str] = Field(None, description="ID of the transfer to delete")
    targetAccountId: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    currency: Optional[str] = Field(None, description="Code of the currency of the borderless account to retrieve the statement of")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profileId: Optional[str] = Field(None, description="ID of the user profile whose account to retrieve the statement of. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    fileName: Optional[str] = Field(None, description="Name of the file that will be downloaded")


class WiseGetstatementTool(BaseTool):
    name = "wise_getstatement"
    description = "Tool for wise getStatement operation - getStatement operation"
    
    def _run(self, **kwargs):
        """Run the wise getStatement operation."""
        # Implement the tool logic here
        return f"Running wise getStatement operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wise getStatement operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
