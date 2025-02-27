from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import YourlsCredentials

class YourlsStatsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    short_url: Optional[str] = Field(None, description="The short URL for which to get stats")
    operation: Optional[str] = Field(None, description="Operation")


class YourlsStatsTool(BaseTool):
    name: str = "yourls_stats"
    connector_id: str = "nodes-base.yourls"
    description: str = "Tool for yourls stats operation - stats operation"
    args_schema: type[BaseModel] | None = YourlsStatsToolInput
    credentials: Optional[YourlsCredentials] = None
