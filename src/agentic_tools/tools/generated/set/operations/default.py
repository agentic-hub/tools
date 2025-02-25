from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SetDefaultToolInput(BaseModel):
    jsonOutput: Optional[str] = Field(None, description="JSON Output")
    duplicateWarning: Optional[str] = Field(None, description="Item duplication is set in the node settings. This option will be ignored when the workflow runs automatically.")
    excludeFields: Optional[str] = Field(None, description="Comma-separated list of the field names you want to exclude from the output. You can drag the selected fields from the input panel.")
    include: Optional[str] = Field(None, description="How to select the fields you want to include in your output items")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    mode: Optional[str] = Field(None, description="Mode")
    includeFields: Optional[str] = Field(None, description="Comma-separated list of the field names you want to include in the output. You can drag the selected fields from the input panel.")
    duplicateItem: Optional[bool] = Field(None, description="Duplicate Item")
    fields: Optional[Dict[str, Any]] = Field(None, description="Edit existing fields or add new ones to modify the output data")
    duplicateCount: Optional[float] = Field(None, description="How many times the item should be duplicated, mainly used for testing and debugging")


class SetDefaultTool(BaseTool):
    name = "set_default"
    description = "Tool for set default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the set default operation."""
        # Implement the tool logic here
        return f"Running set default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the set default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
