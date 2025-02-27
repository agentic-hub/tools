from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GotowebinarCredentials

class GotowebinarUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    panelist_key: Optional[str] = Field(None, description="Key of the panelist to delete")
    details: Optional[str] = Field(None, description="The details to retrieve for the attendee")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The co-organizer's email address")
    webinar_key: Optional[str] = Field(None, description="Key of the webinar that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    session_key: Optional[str] = Field(None, description="Key of the session that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coorganizer_key: Optional[str] = Field(None, description="Key of the co-organizer to delete")
    operation: Optional[str] = Field(None, description="Operation")
    registrant_key: Optional[str] = Field(None, description="Registrant key of the attendee at the webinar session")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    notify_participants: Optional[bool] = Field(None, description="Notify Participants")
    is_external: Optional[bool] = Field(None, description="Whether the co-organizer has no GoToWebinar account")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class GotowebinarUpdateTool(BaseTool):
    name: str = "gotowebinar_update"
    description: str = "Tool for goToWebinar update operation - update operation"
    args_schema: type[BaseModel] | None = GotowebinarUpdateToolInput
    credentials: Optional[GotowebinarCredentials] = None
