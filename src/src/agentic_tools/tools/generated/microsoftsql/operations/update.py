from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftsqlUpdateToolInput(BaseModel):
    updateKey: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be updated. Normally that would be \"id\".")
    table: Optional[str] = Field(None, description="Name of the table in which to update data in")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for rows to update")


class MicrosoftsqlUpdateTool(BaseTool):
    name = "microsoftsql_update"
    description = "Tool for microsoftSql update operation - update operation"
    
    def _run(self, **kwargs):
        """Run the microsoftSql update operation."""
        # Implement the tool logic here
        return f"Running microsoftSql update operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftSql update operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
