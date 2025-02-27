from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarDeleteToolInput(BaseModel):
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarDeleteTool(BaseTool):
    name: str = "googlecalendar_delete"
    connector_id: str = "nodes-base.googleCalendar"
    description: str = "Tool for googleCalendar delete operation - delete operation"
    args_schema: type[BaseModel] | None = GooglecalendarDeleteToolInput
    credentials: Optional[GooglecalendarCredentials] = None
