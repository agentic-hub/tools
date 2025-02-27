from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MarketstackCredentials

class MarketstackGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    symbols: Optional[str] = Field(None, description="One or multiple comma-separated stock symbols (tickers) to retrieve, e.g. <code>AAPL</code> or <code>AAPL,MSFT</code>")
    operation: Optional[str] = Field(None, description="Operation")


class MarketstackGetallTool(BaseTool):
    name: str = "marketstack_getall"
    description: str = "Tool for marketstack getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MarketstackGetallToolInput
    credentials: Optional[MarketstackCredentials] = None
