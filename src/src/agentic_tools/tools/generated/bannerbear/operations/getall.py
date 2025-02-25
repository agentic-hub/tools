from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class BannerbearGetallToolInput(BaseModel):
    templateId: Optional[str] = Field(None, description="The template ID you want to use. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class BannerbearGetallTool(BaseTool):
    name = "bannerbear_getall"
    description = "Tool for bannerbear getAll operation - getAll operation"
    
    def _run(self, **kwargs):
        """Run the bannerbear getAll operation."""
        # Implement the tool logic here
        return f"Running bannerbear getAll operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the bannerbear getAll operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
