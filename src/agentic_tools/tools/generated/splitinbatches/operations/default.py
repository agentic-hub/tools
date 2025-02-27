from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplitinbatchesDefaultToolInput(BaseModel):
    batch_size: Optional[float] = Field(None, description="The number of items to return with each call")
    split_in_batches_notice: Optional[str] = Field(None, description="You may not need this node — n8n nodes automatically run once for each input item. <a href=\"https://docs.n8n.io/getting-started/key-concepts/looping.html#using-loops-in-n8n\" target=\"_blank\">More info</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")


class SplitinbatchesDefaultTool(BaseTool):
    name: str = "splitinbatches_default"
    connector_id: str = "nodes-base.splitInBatches"
    description: str = "Tool for splitInBatches default operation - default operation"
    args_schema: type[BaseModel] | None = SplitinbatchesDefaultToolInput
