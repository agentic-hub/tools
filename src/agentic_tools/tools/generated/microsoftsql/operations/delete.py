from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftsqlDeleteToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to delete data")
    deleteKey: Optional[str] = Field(None, description="Name of the property which decides which rows in the database should be deleted. Normally that would be \"id\".")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlDeleteTool(BaseTool):
    name = "microsoftsql_delete"
    description = "Tool for microsoftSql delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the microsoftSql delete operation."""
        # Implement the tool logic here
        return f"Running microsoftSql delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftSql delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
