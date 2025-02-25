from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BannerbearGetToolInput(BaseModel):
    templateId: Optional[str] = Field(None, description="Unique identifier for the template")
    imageId: Optional[str] = Field(None, description="Unique identifier for the image")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class BannerbearGetTool(BaseTool):
    name = "bannerbear_get"
    description = "Tool for bannerbear get operation - get operation"
    
    def _run(self, **kwargs):
        """Run the bannerbear get operation."""
        # Implement the tool logic here
        return f"Running bannerbear get operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bannerbear get operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
