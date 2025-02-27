from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExecutecommandDefaultToolInput(BaseModel):
    command: Optional[str] = Field(None, description="The command to execute")
    execute_once: Optional[bool] = Field(None, description="Whether to execute only once instead of once for each entry")


class ExecutecommandDefaultTool(BaseTool):
    name: str = "executecommand_default"
    connector_id: str = "nodes-base.executeCommand"
    description: str = "Tool for executeCommand default operation - default operation"
    args_schema: type[BaseModel] | None = ExecutecommandDefaultToolInput
