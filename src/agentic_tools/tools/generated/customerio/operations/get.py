from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CustomerioCredentials

class CustomerioGetToolInput(BaseModel):
    event_name: Optional[str] = Field(None, description="Name of the event to track")
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[float] = Field(None, description="The unique identifier for the campaign")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://github.com/agilecrm/rest-api#1-companys---companies-api\">here</a>")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier for the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class CustomerioGetTool(BaseTool):
    name: str = "customerio_get"
    connector_id: str = "nodes-base.customerIo"
    description: str = "Tool for customerIo get operation - get operation"
    args_schema: type[BaseModel] | None = CustomerioGetToolInput
    credentials: Optional[CustomerioCredentials] = None
