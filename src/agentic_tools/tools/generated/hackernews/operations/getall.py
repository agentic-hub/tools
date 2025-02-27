from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HackernewsGetallToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    resource: Optional[str] = Field(None, description="Resource")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class HackernewsGetallTool(BaseTool):
    name: str = "hackernews_getall"
    description: str = "Tool for hackerNews getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = HackernewsGetallToolInput
