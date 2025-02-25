from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class QuestdbInsertToolInput(BaseModel):
    schema: Optional[str] = Field(None, description="Name of the schema the table belongs to")
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    additionalFields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    returnFields: Optional[str] = Field(None, description="Comma-separated list of the fields that the operation will return")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class QuestdbInsertTool(BaseTool):
    name = "questdb_insert"
    description = "Tool for questDb insert operation - insert operation"
    
    def _run(self, **kwargs):
        """Run the questDb insert operation."""
        # Implement the tool logic here
        return f"Running questDb insert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the questDb insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
