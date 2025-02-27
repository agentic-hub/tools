from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DatetimeFormatdateToolInput(BaseModel):
    time_unit: Optional[str] = Field(None, description="Time unit for Duration parameter below")
    format: Optional[str] = Field(None, description="The format to convert the date to")
    units: Optional[str] = Field(None, description="units")
    date: Optional[str] = Field(None, description="The date that you want to format")
    magnitude: Optional[str] = Field(None, description="The date that you want to change")
    output_field_name: Optional[str] = Field(None, description="Name of the field to put the output in")
    operation: Optional[str] = Field(None, description="Operation")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    custom_format: Optional[str] = Field(None, description="Custom Format")
    notice: Optional[str] = Field(None, description="You can also do this using an expression, e.g. <code>{{your_date.format('yyyy-MM-dd')}}</code>. <a target='_blank' href='https://docs.n8n.io/code-examples/expressions/luxon/'>More info</a>")
    duration: Optional[float] = Field(None, description="The number of time units to add to the date")


class DatetimeFormatdateTool(BaseTool):
    name: str = "datetime_formatdate"
    connector_id: str = "nodes-base.dateTime"
    description: str = "Tool for dateTime formatDate operation - formatDate operation"
    args_schema: type[BaseModel] | None = DatetimeFormatdateToolInput
