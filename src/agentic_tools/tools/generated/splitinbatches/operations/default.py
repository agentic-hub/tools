from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SplitinbatchesDefaultToolInput(BaseModel):
    batchSize: Optional[float] = Field(None, description="The number of items to return with each call")
    splitInBatchesNotice: Optional[str] = Field(None, description="You may not need this node — n8n nodes automatically run once for each input item. <a href=\"https://docs.n8n.io/getting-started/key-concepts/looping.html#using-loops-in-n8n\" target=\"_blank\">More info</a>")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")


class SplitinbatchesDefaultTool(BaseTool):
    name = "splitinbatches_default"
    description = "Tool for splitInBatches default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the splitInBatches default operation."""
        # Implement the tool logic here
        return f"Running splitInBatches default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the splitInBatches default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
