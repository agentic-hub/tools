from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MongodbDeleteToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Add query options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB Delete query")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbDeleteTool(BaseTool):
    name = "mongodb_delete"
    description = "Tool for mongoDb delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the mongoDb delete operation."""
        # Implement the tool logic here
        return f"Running mongoDb delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mongoDb delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
