from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaypalCredentials

class PaypalGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")
    payout_batch_id: Optional[str] = Field(None, description="The ID of the payout for which to show details")
    payout_item_id: Optional[str] = Field(None, description="The ID of the payout item for which to show details")


class PaypalGetTool(BaseTool):
    name: str = "paypal_get"
    description: str = "Tool for payPal get operation - get operation"
    args_schema: type[BaseModel] | None = PaypalGetToolInput
    credentials: Optional[PaypalCredentials] = None
