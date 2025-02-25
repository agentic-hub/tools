from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PaddleRescheduleToolInput(BaseModel):
    discountAmount: Optional[float] = Field(None, description="Discount amount in currency")
    paymentId: Optional[str] = Field(None, description="The upcoming subscription payment ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    date: Optional[str] = Field(None, description="Date you want to move the payment to")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    productIds: Optional[str] = Field(None, description="productIds")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleRescheduleTool(BaseTool):
    name = "paddle_reschedule"
    description = "Tool for paddle reschedule operation - reschedule operation"
    
    def _run(self, **kwargs):
        """Run the paddle reschedule operation."""
        # Implement the tool logic here
        return f"Running paddle reschedule operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the paddle reschedule operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
