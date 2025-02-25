from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MicrosoftsqlExecutequeryToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    query: Optional[str] = Field(None, description="The SQL query to execute")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class MicrosoftsqlExecutequeryTool(BaseTool):
    name = "microsoftsql_executequery"
    description = "Tool for microsoftSql executeQuery operation - executeQuery operation"
    
    def _run(self, **kwargs):
        """Run the microsoftSql executeQuery operation."""
        # Implement the tool logic here
        return f"Running microsoftSql executeQuery operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the microsoftSql executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
