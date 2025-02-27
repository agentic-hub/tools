from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class RssfeedreadDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    url: Optional[str] = Field(None, description="URL of the RSS feed")


class RssfeedreadDefaultTool(BaseTool):
    name: str = "rssfeedread_default"
    connector_id: str = "nodes-base.rssFeedRead"
    description: str = "Tool for rssFeedRead default operation - default operation"
    args_schema: type[BaseModel] | None = RssfeedreadDefaultToolInput
