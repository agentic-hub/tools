from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AdaloCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    dataToSend: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    inputsToIgnore: Optional[str] = Field(None, description="List of input properties to avoid sending, separated by commas. Leave empty to send all properties.")
    collectionId: Optional[str] = Field(None, description="Open your Adalo application and click on the three buttons beside the collection name, then select API Documentation")
    operation: Optional[str] = Field(None, description="Operation")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Field must be defined in the collection, otherwise it will be ignored. If field defined in the collection is not set here, it will be set to null.")


class AdaloCreateTool(BaseTool):
    name = "adalo_create"
    description = "Tool for adalo create operation - create operation"
    
    def _run(self, **kwargs):
        """Run the adalo create operation."""
        # Implement the tool logic here
        return f"Running adalo create operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the adalo create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
