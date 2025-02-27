from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class HackernewsGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    article_id: Optional[str] = Field(None, description="The ID of the Hacker News article to be returned")
    username: Optional[str] = Field(None, description="The Hacker News user to be returned")
    operation: Optional[str] = Field(None, description="Operation")


class HackernewsGetTool(BaseTool):
    name: str = "hackernews_get"
    connector_id: str = "nodes-base.hackerNews"
    description: str = "Tool for hackerNews get operation - get operation"
    args_schema: type[BaseModel] | None = HackernewsGetToolInput
