from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IntervalDefaultToolInput(BaseModel):
    interval: Optional[float] = Field(None, description="Interval value")
    unit: Optional[str] = Field(None, description="Unit of the interval value")
    notice: Optional[str] = Field(None, description="This workflow will run on the schedule you define here once you <a data-key=\"activate\">activate</a> it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'test workflow'")


class IntervalDefaultTool(BaseTool):
    name: str = "interval_default"
    connector_id: str = "nodes-base.interval"
    description: str = "Tool for interval default operation - default operation"
    args_schema: type[BaseModel] | None = IntervalDefaultToolInput
