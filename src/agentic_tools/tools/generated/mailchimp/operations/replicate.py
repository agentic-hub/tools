from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MailchimpCredentials

class MailchimpReplicateToolInput(BaseModel):
    campaign_id: Optional[str] = Field(None, description="List of Campaigns")
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


class MailchimpReplicateTool(BaseTool):
    name: str = "mailchimp_replicate"
    connector_id: str = "nodes-base.mailchimp"
    description: str = "Tool for mailchimp replicate operation - replicate operation"
    args_schema: type[BaseModel] | None = MailchimpReplicateToolInput
    credentials: Optional[MailchimpCredentials] = None
