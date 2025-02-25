from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglebigqueryExecutequeryToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    projectId: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sqlQuery: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")


class GooglebigqueryExecutequeryTool(BaseTool):
    name = "googlebigquery_executequery"
    description = "Tool for googleBigQuery executeQuery operation - executeQuery operation"
    
    def _run(self, **kwargs):
        """Run the googleBigQuery executeQuery operation."""
        # Implement the tool logic here
        return f"Running googleBigQuery executeQuery operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleBigQuery executeQuery operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
