from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NoopDefaultToolInput(BaseModel):


class NoopDefaultTool(BaseTool):
    name: str = "noop_default"
    description: str = "Tool for noOp default operation - default operation"
    args_schema: type[BaseModel] | None = NoopDefaultToolInput
