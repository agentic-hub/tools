from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DatetimeGettimebetweendatesToolInput(BaseModel):
    time_unit: Optional[str] = Field(None, description="Time unit for Duration parameter below")
    units: Optional[str] = Field(None, description="units")
    date: Optional[str] = Field(None, description="The date that you want to format")
    magnitude: Optional[str] = Field(None, description="The date that you want to change")
    output_field_name: Optional[str] = Field(None, description="Name of the field to put the output in")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    end_date: Optional[str] = Field(None, description="End Date")
    start_date: Optional[str] = Field(None, description="Start Date")
    notice: Optional[str] = Field(None, description="You can also refer to the current date in n8n expressions by using <code>{{$now}}</code> or <code>{{$today}}</code>. <a target=\"_blank\" href=\"https://docs.n8n.io/code-examples/expressions/luxon/\">More info</a>")
    duration: Optional[float] = Field(None, description="The number of time units to add to the date")


class DatetimeGettimebetweendatesTool(BaseTool):
    name: str = "datetime_gettimebetweendates"
    description: str = "Tool for dateTime getTimeBetweenDates operation - getTimeBetweenDates operation"
    args_schema: type[BaseModel] | None = DatetimeGettimebetweendatesToolInput
