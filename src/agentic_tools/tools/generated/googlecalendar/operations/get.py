from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarGetToolInput(BaseModel):
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarGetTool(BaseTool):
    name: str = "googlecalendar_get"
    description: str = "Tool for googleCalendar get operation - get operation"
    args_schema: type[BaseModel] | None = GooglecalendarGetToolInput
    credentials: Optional[GooglecalendarCredentials] = None
