from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class PostgresDeletetableToolInput(BaseModel):
    table: Optional[str] = Field(None, description="By Name")
    valuesToSend: Optional[Dict[str, Any]] = Field(None, description="Values to Send")
    restartSequences: Optional[bool] = Field(None, description="Whether to reset identity (auto-increment) columns to their initial values")
    operation: Optional[str] = Field(None, description="Operation")
    schema: Optional[str] = Field(None, description="By Name")
    where: Optional[Dict[str, Any]] = Field(None, description="If not set, all rows will be selected")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    deleteCommand: Optional[str] = Field(None, description="Command")
    columns: Optional[str] = Field(None, description="columns")
    dataMode: Optional[str] = Field(None, description="Whether to map node input properties and the table data automatically or manually")
    resource: Optional[str] = Field(None, description="Resource")
    combineConditions: Optional[str] = Field(None, description="How to combine the conditions defined in \"Select Rows\": AND requires all conditions to be true, OR requires at least one condition to be true")
    columnToMatchOn: Optional[str] = Field(None, description="The column to compare when finding the rows to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\" target=\"_blank\">expression</a>.")
    valueToMatchOn: Optional[str] = Field(None, description="Rows with a value in the specified \"Column to Match On\" that corresponds to the value in this field will be updated")
    notice: Optional[str] = Field(None, description="
		In this mode, make sure incoming data fields are named the same as the columns in your table. If needed, use an 'Edit Fields' node before this node to change the field names.
		")


class PostgresDeletetableTool(BaseTool):
    name = "postgres_deletetable"
    description = "Tool for postgres deleteTable operation - deleteTable operation"
    
    def _run(self, **kwargs):
        """Run the postgres deleteTable operation."""
        # Implement the tool logic here
        return f"Running postgres deleteTable operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the postgres deleteTable operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
