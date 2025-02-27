from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CustomerioCredentials

class CustomerioAddToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="Name of the event to track")
    customer_ids: Optional[str] = Field(None, description="A list of customer IDs to add to the segment")
    segment_id: Optional[float] = Field(None, description="The unique identifier of the segment")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioAddTool(BaseTool):
    name: str = "customerio_add"
    description: str = "Tool for customerIo add operation - add operation"
    args_schema: type[BaseModel] | None = CustomerioAddToolInput
    credentials: Optional[CustomerioCredentials] = None
