from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class WiseGetToolInput(BaseModel):
    quoteId: Optional[str] = Field(None, description="ID of the quote to retrieve")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binaryProperty: Optional[str] = Field(None, description="Put Output File in Field")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    target: Optional[str] = Field(None, description="Code of the target currency to retrieve the exchange rate for")
    transferId: Optional[str] = Field(None, description="ID of the transfer to retrieve")
    targetAccountId: Optional[str] = Field(None, description="ID of the account that will receive the funds. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    source: Optional[str] = Field(None, description="Code of the source currency to retrieve the exchange rate for")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    profileId: Optional[str] = Field(None, description="ID of the user profile to retrieve. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    fileName: Optional[str] = Field(None, description="Name of the file that will be downloaded")
    downloadReceipt: Optional[bool] = Field(None, description="Whether to download the transfer receipt as a PDF file. Only for executed transfers, having status 'Outgoing Payment Sent'.")


class WiseGetTool(BaseTool):
    name = "wise_get"
    description = "Tool for wise get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the wise get operation."""
        # Implement the tool logic here
        return f"Running wise get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the wise get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
