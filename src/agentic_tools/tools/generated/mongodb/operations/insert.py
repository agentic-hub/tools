from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MongodbInsertToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbInsertTool(BaseTool):
    name = "mongodb_insert"
    description = "Tool for mongoDb insert operation - insert operation"
    
    def _run(self, **kwargs):
        """Run the mongoDb insert operation."""
        # Implement the tool logic here
        return f"Running mongoDb insert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mongoDb insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
