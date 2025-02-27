from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DatetimeGetcurrentdateToolInput(BaseModel):
    time_unit: Optional[str] = Field(None, description="Time unit for Duration parameter below")
    include_time: Optional[bool] = Field(None, description="When deactivated, the time will be set to midnight")
    units: Optional[str] = Field(None, description="units")
    date: Optional[str] = Field(None, description="The date that you want to format")
    magnitude: Optional[str] = Field(None, description="The date that you want to change")
    output_field_name: Optional[str] = Field(None, description="Name of the field to put the output in")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    notice: Optional[str] = Field(None, description="You can also refer to the current date in n8n expressions by using <code>{{$now}}</code> or <code>{{$today}}</code>. <a target=\"_blank\" href=\"https://docs.n8n.io/code-examples/expressions/luxon/\">More info</a>")
    duration: Optional[float] = Field(None, description="The number of time units to add to the date")


class DatetimeGetcurrentdateTool(BaseTool):
    name: str = "datetime_getcurrentdate"
    description: str = "Tool for dateTime getCurrentDate operation - getCurrentDate operation"
    args_schema: type[BaseModel] | None = DatetimeGetcurrentdateToolInput
