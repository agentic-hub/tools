from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaddleCredentials

class PaddleRescheduleToolInput(BaseModel):
    discount_amount: Optional[float] = Field(None, description="Discount amount in currency")
    payment_id: Optional[str] = Field(None, description="The upcoming subscription payment ID. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    date: Optional[str] = Field(None, description="Date you want to move the payment to")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Attributes in JSON form")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    product_ids: Optional[str] = Field(None, description="productIds")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class PaddleRescheduleTool(BaseTool):
    name: str = "paddle_reschedule"
    description: str = "Tool for paddle reschedule operation - reschedule operation"
    args_schema: type[BaseModel] | None = PaddleRescheduleToolInput
    credentials: Optional[PaddleCredentials] = None
