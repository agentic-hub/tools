from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ChargebeePdfurlToolInput(BaseModel):
    invoiceId: Optional[str] = Field(None, description="The ID of the invoice to get")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    subscriptionId: Optional[str] = Field(None, description="The ID of the subscription to cancel")


class ChargebeePdfurlTool(BaseTool):
    name = "chargebee_pdfurl"
    description = "Tool for chargebee pdfUrl operation - pdfUrl operation"
    
    def _run(self, **kwargs):
        """Run the chargebee pdfUrl operation."""
        # Implement the tool logic here
        return f"Running chargebee pdfUrl operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the chargebee pdfUrl operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
