from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MetabaseCredentials

class MetabaseGetallToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseGetallTool(BaseTool):
    name: str = "metabase_getall"
    description: str = "Tool for metabase getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MetabaseGetallToolInput
    credentials: Optional[MetabaseCredentials] = None
