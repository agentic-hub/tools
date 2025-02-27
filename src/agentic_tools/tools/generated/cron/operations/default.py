from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CronDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="This workflow will run on the schedule you define here once you <a data-key=\"activate\">activate</a> it.<br><br>For testing, you can also trigger it manually: by going back to the canvas and clicking 'test workflow'")
    trigger_times: Optional[Dict[str, Any]] = Field(None, description="Triggers for the workflow")


class CronDefaultTool(BaseTool):
    name: str = "cron_default"
    description: str = "Tool for cron default operation - default operation"
    args_schema: type[BaseModel] | None = CronDefaultToolInput
