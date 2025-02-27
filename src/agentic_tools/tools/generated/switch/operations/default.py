from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SwitchDefaultToolInput(BaseModel):
    output: Optional[float] = Field(None, description="The output index to send the input item to. Use an expression to calculate which input item should be routed to which output. The expression must return a number.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    number_outputs: Optional[float] = Field(None, description="How many outputs to create")
    rules: Optional[Dict[str, Any]] = Field(None, description="Routing Rules")
    mode: Optional[str] = Field(None, description="How data should be routed")


class SwitchDefaultTool(BaseTool):
    name: str = "switch_default"
    connector_id: str = "nodes-base.switch"
    description: str = "Tool for switch default operation - default operation"
    args_schema: type[BaseModel] | None = SwitchDefaultToolInput
