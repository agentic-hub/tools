from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglesheetstriggerDefaultToolInput(BaseModel):
    includeInOutput: Optional[str] = Field(None, description="This option will be effective only when automatically executing the workflow")
    sheetName: Optional[str] = Field(None, description="By URL")
    pollTimes: Optional[Dict[str, Any]] = Field(None, description="Time at which polling should occur")
    event: Optional[str] = Field(None, description="It will be triggered also by newly created columns (if the 'Columns to Watch' option is not set)")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    documentId: Optional[str] = Field(None, description="By URL")


class GooglesheetstriggerDefaultTool(BaseTool):
    name = "googlesheetstrigger_default"
    description = "Tool for googleSheetsTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the googleSheetsTrigger default operation."""
        # Implement the tool logic here
        return f"Running googleSheetsTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleSheetsTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
