from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaddleCredentials

class PaddleUpdateToolInput(BaseModel):
    discount_amount: Optional[float] = Field(None, description="Discount amount in currency")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_by: Optional[str] = Field(None, description="Either flat or percentage")
    product_ids: Optional[str] = Field(None, description="productIds")
    group: Optional[str] = Field(None, description="The name of the group of coupons you want to update")
    coupon_code: Optional[str] = Field(None, description="Identify the coupon to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleUpdateTool(BaseTool):
    name: str = "paddle_update"
    description: str = "Tool for paddle update operation - update operation"
    args_schema: type[BaseModel] | None = PaddleUpdateToolInput
    credentials: Optional[PaddleCredentials] = None
