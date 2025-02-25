from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MetabaseGetToolInput(BaseModel):
    questionId: Optional[str] = Field(None, description="Question ID")
    metricId: Optional[str] = Field(None, description="Metric ID")
    alertId: Optional[str] = Field(None, description="Alert ID")
    operation: Optional[str] = Field(None, description="Operation")
    resource: Optional[str] = Field(None, description="Resource")


class MetabaseGetTool(BaseTool):
    name = "metabase_get"
    description = "Tool for metabase get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the metabase get operation."""
        # Implement the tool logic here
        return f"Running metabase get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the metabase get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
