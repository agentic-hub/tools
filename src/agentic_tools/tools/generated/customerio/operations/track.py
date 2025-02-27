from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CustomerioCredentials

class CustomerioTrackToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="Name of the event to track")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    customer_id: Optional[str] = Field(None, description="The unique identifier for the customer")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://customer.io/docs/api-triggered-data-format#basic-data-formatting\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioTrackTool(BaseTool):
    name: str = "customerio_track"
    connector_id: str = "nodes-base.customerIo"
    description: str = "Tool for customerIo track operation - track operation"
    args_schema: type[BaseModel] | None = CustomerioTrackToolInput
    credentials: Optional[CustomerioCredentials] = None
