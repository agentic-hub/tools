from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaddleCredentials

class PaddleGetallToolInput(BaseModel):
    discount_amount: Optional[float] = Field(None, description="Discount amount in currency")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    product_ids: Optional[str] = Field(None, description="productIds")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    product_id: Optional[str] = Field(None, description="The specific product/subscription ID")


class PaddleGetallTool(BaseTool):
    name: str = "paddle_getall"
    description: str = "Tool for paddle getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = PaddleGetallToolInput
    credentials: Optional[PaddleCredentials] = None
