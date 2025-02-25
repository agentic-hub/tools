from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class GooglebigqueryInsertToolInput(BaseModel):
    dataMode: Optional[str] = Field(None, description="Whether to insert the input data this node receives in the new row")
    resource: Optional[str] = Field(None, description="Resource")
    tableId: Optional[str] = Field(None, description="By ID")
    datasetId: Optional[str] = Field(None, description="By ID")
    projectId: Optional[str] = Field(None, description="By URL")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    sqlQuery: Optional[str] = Field(None, description="SQL query to execute, you can find more information <a href=\"https://cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax\" target=\"_blank\">here</a>. Standard SQL syntax used by default, but you can also use Legacy SQL syntax by using optinon 'Use Legacy SQL'.")
    operation: Optional[str] = Field(None, description="Operation")
    info: Optional[str] = Field(None, description="In this mode, make sure the incoming data fields are named the same as the columns in BigQuery. (Use an 'Edit Fields' node before this node to change them if required.)")
    fieldsUi: Optional[Dict[str, Any]] = Field(None, description="Fields to Send")


class GooglebigqueryInsertTool(BaseTool):
    name = "googlebigquery_insert"
    description = "Tool for googleBigQuery insert operation - insert operation"
    
    def _run(self, **kwargs):
        """Run the googleBigQuery insert operation."""
        # Implement the tool logic here
        return f"Running googleBigQuery insert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the googleBigQuery insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
