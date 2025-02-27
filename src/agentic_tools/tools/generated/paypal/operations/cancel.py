from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaypalCredentials

class PaypalCancelToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")
    payout_item_id: Optional[str] = Field(None, description="The ID of the payout item to cancel")


class PaypalCancelTool(BaseTool):
    name: str = "paypal_cancel"
    connector_id: str = "nodes-base.payPal"
    description: str = "Tool for payPal cancel operation - cancel operation"
    args_schema: type[BaseModel] | None = PaypalCancelToolInput
    credentials: Optional[PaypalCredentials] = None
