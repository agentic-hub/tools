from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GooglecalendarCredentials

class GooglecalendarUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    use_default_reminders: Optional[bool] = Field(None, description="Use Default Reminders")
    event_id: Optional[str] = Field(None, description="Event ID")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar: Optional[Dict[str, Any]] = Field(None, description="Google Calendar to operate on")
    reminders_ui: Optional[Dict[str, Any]] = Field(None, description="If the event doesn't use the default reminders, this lists the reminders specific to the event")
    operation: Optional[str] = Field(None, description="Operation")


class GooglecalendarUpdateTool(BaseTool):
    name: str = "googlecalendar_update"
    description: str = "Tool for googleCalendar update operation - update operation"
    args_schema: type[BaseModel] | None = GooglecalendarUpdateToolInput
    credentials: Optional[GooglecalendarCredentials] = None
