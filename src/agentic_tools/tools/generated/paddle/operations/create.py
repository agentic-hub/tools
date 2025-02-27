from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaddleCredentials

class PaddleCreateToolInput(BaseModel):
    discount_amount: Optional[float] = Field(None, description="Discount amount in currency")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    coupon_type: Optional[str] = Field(None, description="Either product (valid for specified products or subscription plans) or checkout (valid for any checkout)")
    additional_fields_json: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    product_ids: Optional[str] = Field(None, description="productIds")
    discount_type: Optional[str] = Field(None, description="Either flat or percentage")
    currency: Optional[str] = Field(None, description="The currency must match the balance currency specified in your account")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleCreateTool(BaseTool):
    name: str = "paddle_create"
    description: str = "Tool for paddle create operation - create operation"
    args_schema: type[BaseModel] | None = PaddleCreateToolInput
    credentials: Optional[PaddleCredentials] = None
