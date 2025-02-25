from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PaddleGetToolInput(BaseModel):
    discountAmount: Optional[float] = Field(None, description="Discount amount in currency")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    planId: Optional[str] = Field(None, description="Filter: The subscription plan ID")
    productIds: Optional[str] = Field(None, description="productIds")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleGetTool(BaseTool):
    name = "paddle_get"
    description = "Tool for paddle get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the paddle get operation."""
        # Implement the tool logic here
        return f"Running paddle get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the paddle get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
