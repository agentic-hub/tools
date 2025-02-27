from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StartDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="This node is where a manual workflow execution starts. To make one, go back to the canvas and click ‘execute workflow’")


class StartDefaultTool(BaseTool):
    name: str = "start_default"
    connector_id: str = "nodes-base.start"
    description: str = "Tool for start default operation - default operation"
    args_schema: type[BaseModel] | None = StartDefaultToolInput
