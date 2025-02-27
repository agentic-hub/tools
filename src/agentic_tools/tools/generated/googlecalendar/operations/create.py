from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarCreateToolInput(BaseModel):
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    start: Optional[str] = Field(None, description="Start time of the event")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    end: Optional[str] = Field(None, description="End time of the event")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarCreateTool(BaseTool):
    name: str = "googlecalendar_create"
    description: str = "Tool for googleCalendar create operation - create operation"
    args_schema: type[BaseModel] | None = GooglecalendarCreateToolInput
    credentials: Optional[GooglecalendarCredentials] = None
