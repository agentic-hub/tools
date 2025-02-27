from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MarketstackCredentials

class MarketstackGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    exchange: Optional[str] = Field(None, description="Stock exchange to retrieve, specified by <a href=\"https://en.wikipedia.org/wiki/Market_Identifier_Code\">Market Identifier Code</a>, e.g. <code>XNAS</code>")
    operation: Optional[str] = Field(None, description="Operation")
    symbol: Optional[str] = Field(None, description="Stock symbol (ticker) to retrieve, e.g. <code>AAPL</code>")


class MarketstackGetTool(BaseTool):
    name: str = "marketstack_get"
    connector_id: str = "nodes-base.marketstack"
    description: str = "Tool for marketstack get operation - get operation"
    args_schema: type[BaseModel] | None = MarketstackGetToolInput
    credentials: Optional[MarketstackCredentials] = None
