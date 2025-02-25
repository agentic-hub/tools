from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GotowebinarReinviteToolInput(BaseModel):
    panelistKey: Optional[str] = Field(None, description="Key of the panelist to reinvite")
    details: Optional[str] = Field(None, description="The details to retrieve for the attendee")
    returnAll: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="The co-organizer's email address")
    webinarKey: Optional[str] = Field(None, description="Key of the webinar that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    sessionKey: Optional[str] = Field(None, description="Key of the session that the attendee attended. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    coorganizerKey: Optional[str] = Field(None, description="Key of the co-organizer to reinvite")
    operation: Optional[str] = Field(None, description="Operation")
    registrantKey: Optional[str] = Field(None, description="Registrant key of the attendee at the webinar session")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    isExternal: Optional[bool] = Field(None, description="Whether the co-organizer has no GoToWebinar account")
    resource: Optional[str] = Field(None, description="Resource")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class GotowebinarReinviteTool(BaseTool):
    name = "gotowebinar_reinvite"
    description = "Tool for goToWebinar reinvite operation - reinvite operation"
    
    def _run(self, **kwargs):
        """Run the goToWebinar reinvite operation."""
        # Implement the tool logic here
        return f"Running goToWebinar reinvite operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the goToWebinar reinvite operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
