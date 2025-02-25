from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MongodbUpdateToolInput(BaseModel):
    updateKey: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    upsert: Optional[bool] = Field(None, description="Whether to perform an insert if no documents match the update key")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    collection: Optional[str] = Field(None, description="MongoDB Collection")
    fields: Optional[str] = Field(None, description="Comma-separated list of the fields to be included into the new document")
    query: Optional[str] = Field(None, description="MongoDB aggregation pipeline query in JSON format")
    operation: Optional[str] = Field(None, description="Operation")


class MongodbUpdateTool(BaseTool):
    name = "mongodb_update"
    description = "Tool for mongoDb update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the mongoDb update operation."""
        # Implement the tool logic here
        return f"Running mongoDb update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mongoDb update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
