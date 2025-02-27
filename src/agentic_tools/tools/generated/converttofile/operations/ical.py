from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ConverttofileIcalToolInput(BaseModel):
    start: Optional[str] = Field(None, description="Date and time at which the event begins. (For all-day events, the time will be ignored.).")
    all_day: Optional[bool] = Field(None, description="Whether the event lasts all day or not")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Options")
    binary_property_name: Optional[str] = Field(None, description="The field that your iCalendar file will be available under in the output")
    end: Optional[str] = Field(None, description="Date and time at which the event ends. (For all-day events, the time will be ignored.).")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    title: Optional[str] = Field(None, description="Event Title")
    operation: Optional[str] = Field(None, description="Operation")


class ConverttofileIcalTool(BaseTool):
    name: str = "converttofile_ical"
    connector_id: str = "nodes-base.convertToFile"
    description: str = "Tool for convertToFile iCal operation - iCal operation"
    args_schema: type[BaseModel] | None = ConverttofileIcalToolInput
