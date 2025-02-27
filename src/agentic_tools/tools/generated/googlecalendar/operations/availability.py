from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarAvailabilityToolInput(BaseModel):
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    time_max: Optional[str] = Field(None, description="End of the interval")
    time_min: Optional[str] = Field(None, description="Start of the interval")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarAvailabilityTool(BaseTool):
    name: str = "googlecalendar_availability"
    description: str = "Tool for googleCalendar availability operation - availability operation"
    args_schema: type[BaseModel] | None = GooglecalendarAvailabilityToolInput
    credentials: Optional[GooglecalendarCredentials] = None
