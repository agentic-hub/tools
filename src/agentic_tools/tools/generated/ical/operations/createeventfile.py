from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IcalCreateeventfileToolInput(BaseModel):
    start: Optional[str] = Field(None, description="Date and time at which the event begins. (For all-day events, the time will be ignored.).")
    all_day: Optional[bool] = Field(None, description="Whether the event lasts all day or not")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Options")
    end: Optional[str] = Field(None, description="Date and time at which the event ends. (For all-day events, the time will be ignored.).")
    binary_property_name: Optional[str] = Field(None, description="The field that your iCalendar file will be available under in the output")
    title: Optional[str] = Field(None, description="Event Title")
    operation: Optional[str] = Field(None, description="Operation")


class IcalCreateeventfileTool(BaseTool):
    name: str = "ical_createeventfile"
    connector_id: str = "nodes-base.iCal"
    description: str = "Tool for iCal createEventFile operation - createEventFile operation"
    args_schema: type[BaseModel] | None = IcalCreateeventfileToolInput
