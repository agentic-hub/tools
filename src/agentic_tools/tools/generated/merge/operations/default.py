from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MergeDefaultToolInput(BaseModel):
    output: Optional[str] = Field(None, description="Output")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    combinationMode: Optional[str] = Field(None, description="Combination Mode")
    mergeByFields: Optional[Dict[str, Any]] = Field(None, description="Fields to Match")
    joinMode: Optional[str] = Field(None, description="Output Type")
    outputDataFrom: Optional[str] = Field(None, description="Output Data From")
    mode: Optional[str] = Field(None, description="How data of branches should be merged")
    chooseBranchMode: Optional[str] = Field(None, description="Output Type")


class MergeDefaultTool(BaseTool):
    name = "merge_default"
    description = "Tool for merge default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the merge default operation."""
        # Implement the tool logic here
        return f"Running merge default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the merge default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
