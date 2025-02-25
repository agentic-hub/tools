from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BrandfetchFontToolInput(BaseModel):
    imageTypes: Optional[str] = Field(None, description="imageTypes")
    imageFormats: Optional[str] = Field(None, description="imageFormats")
    operation: Optional[str] = Field(None, description="Operation")
    domain: Optional[str] = Field(None, description="The domain name of the company")


class BrandfetchFontTool(BaseTool):
    name = "brandfetch_font"
    description = "Tool for Brandfetch font operation - font operation"
    
    def _run(self, **kwargs):
        """Run the Brandfetch font operation."""
        # Implement the tool logic here
        return f"Running Brandfetch font operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the Brandfetch font operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
