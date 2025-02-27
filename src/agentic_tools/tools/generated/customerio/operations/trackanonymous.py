from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CustomerioCredentials

class CustomerioTrackanonymousToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="The unique identifier for the customer")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://customer.io/docs/api-triggered-data-format#basic-data-formatting\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioTrackanonymousTool(BaseTool):
    name: str = "customerio_trackanonymous"
    description: str = "Tool for customerIo trackAnonymous operation - trackAnonymous operation"
    args_schema: type[BaseModel] | None = CustomerioTrackanonymousToolInput
    credentials: Optional[CustomerioCredentials] = None
