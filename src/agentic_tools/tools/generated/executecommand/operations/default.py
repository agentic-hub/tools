from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExecutecommandDefaultToolInput(BaseModel):
    command: Optional[str] = Field(None, description="The command to execute")
    execute_once: Optional[bool] = Field(None, description="Whether to execute only once instead of once for each entry")


class ExecutecommandDefaultTool(BaseTool):
    name = "executecommand_default"
    description = "Tool for executeCommand default operation - default operation"
    
    def __init__(self, **kwargs):
        """Initialize the tool.
        
        Args:
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
    
    def _run(self, **kwargs):
        """Run the executeCommand default operation."""
        # Implement the tool logic here
        return f"Running executeCommand default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the executeCommand default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
