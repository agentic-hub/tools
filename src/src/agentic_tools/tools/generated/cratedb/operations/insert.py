from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CratedbInsertToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnFields: Optional[str] = Field(None, description="Comma-separated list of the fields that the operation will return")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class CratedbInsertTool(BaseTool):
    name = "cratedb_insert"
    description = "Tool for crateDb insert operation - insert operation"
    
    def _run(self, **kwargs):
        """Run the crateDb insert operation."""
        # Implement the tool logic here
        return f"Running crateDb insert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the crateDb insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
