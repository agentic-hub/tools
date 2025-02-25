from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class IterableAddToolInput(BaseModel):
    userId: Optional[str] = Field(None, description="Unique identifier for a particular user")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[str] = Field(None, description="Value")
    by: Optional[str] = Field(None, description="Identifier to be used")
    listId: Optional[str] = Field(None, description="Identifier to be used. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    identifier: Optional[str] = Field(None, description="Identifier to be used")
    email: Optional[str] = Field(None, description="Email for a particular user")
    operation: Optional[str] = Field(None, description="Operation")


class IterableAddTool(BaseTool):
    name = "iterable_add"
    description = "Tool for iterable add operation - add operation"
    
    def _run(self, **kwargs):
        """Run the iterable add operation."""
        # Implement the tool logic here
        return f"Running iterable add operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the iterable add operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
