from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class CratedbExecutequeryToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    query: Optional[str] = Field(None, description="The SQL query to execute. You can use n8n expressions or $1 and $2 in conjunction with query parameters.")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class CratedbExecutequeryTool(BaseTool):
    name = "cratedb_executequery"
    description = "Tool for crateDb executeQuery operation - executeQuery operation"
    
    def _run(self, **kwargs):
        """Run the crateDb executeQuery operation."""
        # Implement the tool logic here
        return f"Running crateDb executeQuery operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the crateDb executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
