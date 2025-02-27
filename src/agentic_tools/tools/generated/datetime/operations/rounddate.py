from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DatetimeRounddateToolInput(BaseModel):
    time_unit: Optional[str] = Field(None, description="Time unit for Duration parameter below")
    units: Optional[str] = Field(None, description="units")
    mode: Optional[str] = Field(None, description="Mode")
    date: Optional[str] = Field(None, description="The date that you want to round")
    magnitude: Optional[str] = Field(None, description="The date that you want to change")
    output_field_name: Optional[str] = Field(None, description="Name of the field to put the output in")
    operation: Optional[str] = Field(None, description="Operation")
    to_nearest: Optional[str] = Field(None, description="To Nearest")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    to: Optional[str] = Field(None, description="To")
    notice: Optional[str] = Field(None, description="You can also do this using an expression, e.g. <code>{{ your_date.beginningOf('month') }}</code> or <code>{{ your_date.endOfMonth() }}</code>. <a target='_blank' href='https://docs.n8n.io/code-examples/expressions/luxon/'>More info</a>")
    duration: Optional[float] = Field(None, description="The number of time units to add to the date")


class DatetimeRounddateTool(BaseTool):
    name: str = "datetime_rounddate"
    description: str = "Tool for dateTime roundDate operation - roundDate operation"
    args_schema: type[BaseModel] | None = DatetimeRounddateToolInput
