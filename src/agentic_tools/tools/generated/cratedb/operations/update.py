from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CratedbUpdateToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    updateKey: Optional[str] = Field(None, description="Comma-separated list of the properties which decides which rows in the database should be updated. Normally that would be \"id\".")
    table: Optional[str] = Field(None, description="Name of the table in which to update data in")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnFields: Optional[str] = Field(None, description="Comma-separated list of the fields that the operation will return")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for rows to update")


class CratedbUpdateTool(BaseTool):
    name = "cratedb_update"
    description = "Tool for crateDb update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the crateDb update operation."""
        # Implement the tool logic here
        return f"Running crateDb update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the crateDb update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
