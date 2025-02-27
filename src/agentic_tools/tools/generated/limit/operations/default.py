from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class LimitDefaultToolInput(BaseModel):
    keep: Optional[str] = Field(None, description="When removing items, whether to keep the ones at the start or the ending")
    max_items: Optional[float] = Field(None, description="If there are more items than this number, some are removed")


class LimitDefaultTool(BaseTool):
    name: str = "limit_default"
    connector_id: str = "nodes-base.limit"
    description: str = "Tool for limit default operation - default operation"
    args_schema: type[BaseModel] | None = LimitDefaultToolInput
