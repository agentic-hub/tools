from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class FunctionitemDefaultToolInput(BaseModel):
    notice: Optional[str] = Field(None, description="A newer version of this node type is available, called the ‘Code’ node")
    function_code: Optional[str] = Field(None, description="The JavaScript code to execute for each item")


class FunctionitemDefaultTool(BaseTool):
    name: str = "functionitem_default"
    connector_id: str = "nodes-base.functionItem"
    description: str = "Tool for functionItem default operation - default operation"
    args_schema: type[BaseModel] | None = FunctionitemDefaultToolInput
