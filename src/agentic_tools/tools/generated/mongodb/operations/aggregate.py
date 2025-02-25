from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MongodbAggregateToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Add query options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbAggregateTool(BaseTool):
    name = "mongodb_aggregate"
    description = "Tool for mongoDb aggregate operation - aggregate operation"
    
    def _run(self, **kwargs):
        """Run the mongoDb aggregate operation."""
        # Implement the tool logic here
        return f"Running mongoDb aggregate operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mongoDb aggregate operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
