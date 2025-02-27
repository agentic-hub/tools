from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GotowebinarCredentials

class GotowebinarDeleteToolInput(BaseModel):
    panelist_key: Optional[str] = Field(None, description="Key of the panelist to delete")
    details: Optional[str] = Field(None, description="The details to retrieve for the attendee")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The co-organizer's email address")
    webinar_key: Optional[str] = Field(None, description="Key of the webinar that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    session_key: Optional[str] = Field(None, description="Key of the session that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coorganizer_key: Optional[str] = Field(None, description="Key of the co-organizer to delete")
    operation: Optional[str] = Field(None, description="Operation")
    registrant_key: Optional[str] = Field(None, description="Key of the registrant to delete")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    is_external: Optional[bool] = Field(None, description="By default only internal co-organizers (with a GoToWebinar account) can be deleted. If you want to use this call for external co-organizers you have to set this parameter to 'true'.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class GotowebinarDeleteTool(BaseTool):
    name: str = "gotowebinar_delete"
    description: str = "Tool for goToWebinar delete operation - delete operation"
    args_schema: type[BaseModel] | None = GotowebinarDeleteToolInput
    credentials: Optional[GotowebinarCredentials] = None
