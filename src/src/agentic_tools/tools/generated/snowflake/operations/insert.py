from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SnowflakeInsertToolInput(BaseModel):
    table: Optional[str] = Field(None, description="Name of the table in which to insert data to")
    operation: Optional[str] = Field(None, description="Operation")
    columns: Optional[str] = Field(None, description="Comma-separated list of the properties which should used as columns for the new rows")


class SnowflakeInsertTool(BaseTool):
    name = "snowflake_insert"
    description = "Tool for snowflake insert operation - insert operation"
    
    def _run(self, **kwargs):
        """Run the snowflake insert operation."""
        # Implement the tool logic here
        return f"Running snowflake insert operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the snowflake insert operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
