from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class StopanderrorDefaultToolInput(BaseModel):
    error_message: Optional[str] = Field(None, description="Error Message")
    error_type: Optional[str] = Field(None, description="Type of error to throw")
    error_object: Optional[str] = Field(None, description="Object containing error properties")


class StopanderrorDefaultTool(BaseTool):
    name: str = "stopanderror_default"
    connector_id: str = "nodes-base.stopAndError"
    description: str = "Tool for stopAndError default operation - default operation"
    args_schema: type[BaseModel] | None = StopanderrorDefaultToolInput
