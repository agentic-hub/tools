from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailchimpCredentials

class Mailchimp__custom_api_call__ToolInput(BaseModel):
    group_json: Optional[str] = Field(None, description="Interest Groups")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    list: Optional[str] = Field(None, description="List of lists. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email address for a subscriber")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    merge_fields_json: Optional[str] = Field(None, description="Merge Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    location_json: Optional[str] = Field(None, description="Location")


class Mailchimp__custom_api_call__Tool(BaseTool):
    name: str = "mailchimp___custom_api_call__"
    description: str = "Tool for mailchimp __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Mailchimp__custom_api_call__ToolInput
    credentials: Optional[MailchimpCredentials] = None
