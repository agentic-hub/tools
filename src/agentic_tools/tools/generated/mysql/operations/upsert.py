from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MysqlUpsertToolInput(BaseModel):
    dataMode: Optional[str] = Field(None, description="Whether to map node input properties and the table data automatically or manually")
    resource: Optional[str] = Field(None, description="Resource")
    table: Optional[str] = Field(None, description="Name")
    combineConditions: Optional[str] = Field(None, description="How to combine the conditions defined in \"Select Rows\": AND requires all conditions to be true, OR requires at least one condition to be true")
    where: Optional[Dict[str, Any]] = Field(None, description="If not set, all rows will be selected")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    columnToMatchOn: Optional[str] = Field(None, description="The column to compare when finding the rows to update. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\" target=\"_blank\">expression</a>.")
    valueToMatchOn: Optional[str] = Field(None, description="Rows with a value in the specified \"Column to Match On\" that corresponds to the value in this field will be updated. New rows will be created for non-matching items.")
    notice: Optional[str] = Field(None, description="
		In this mode, make sure incoming data fields are named the same as the columns in your table. If needed, use an 'Edit Fields' node before this node to change the field names.
		")
    operation: Optional[str] = Field(None, description="Operation")
    valuesToSend: Optional[Dict[str, Any]] = Field(None, description="Values to Send")


class MysqlUpsertTool(BaseTool):
    name = "mysql_upsert"
    description = "Tool for mySql upsert operation - upsert operation"
    
    def _run(self, **kwargs):
        """Run the mySql upsert operation."""
        # Implement the tool logic here
        return f"Running mySql upsert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mySql upsert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
