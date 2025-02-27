from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarGetallToolInput(BaseModel):
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarGetallTool(BaseTool):
    name: str = "googlecalendar_getall"
    description: str = "Tool for googleCalendar getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GooglecalendarGetallToolInput
    credentials: Optional[GooglecalendarCredentials] = None
