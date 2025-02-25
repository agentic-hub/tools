from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PaddleGetallToolInput(BaseModel):
    discountAmount: Optional[float] = Field(None, description="Discount amount in currency")
    jsonParameters: Optional[bool] = Field(None, description="JSON Parameters")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additionalFieldsJson: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    productIds: Optional[str] = Field(None, description="productIds")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    productId: Optional[str] = Field(None, description="The specific product/subscription ID")


class PaddleGetallTool(BaseTool):
    name = "paddle_getall"
    description = "Tool for paddle getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the paddle getAll operation."""
        # Implement the tool logic here
        return f"Running paddle getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the paddle getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
