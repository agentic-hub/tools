from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FunctionDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="A newer version of this node type is available, called the ‘Code’ node")
    function_code: Optional[str] = Field(None, description="The JavaScript code to execute")


class FunctionDefaultTool(BaseTool):
    name: str = "function_default"
    description: str = "Tool for function default operation - default operation"
    args_schema: type[BaseModel] | None = FunctionDefaultToolInput
