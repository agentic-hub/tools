from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PaypalCredentials

class PaypalCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    sender_batch_id: Optional[str] = Field(None, description="A sender-specified ID number. Tracks the payout in an accounting system.")
    items_ui: Optional[Dict[str, Any]] = Field(None, description="Items")
    items_json: Optional[str] = Field(None, description="An array of individual payout items")
    operation: Optional[str] = Field(None, description="Operation")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    payout_item_id: Optional[str] = Field(None, description="The ID of the payout item for which to show details")


class PaypalCreateTool(BaseTool):
    name: str = "paypal_create"
    description: str = "Tool for payPal create operation - create operation"
    args_schema: type[BaseModel] | None = PaypalCreateToolInput
    credentials: Optional[PaypalCredentials] = None
