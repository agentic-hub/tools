from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class NoopDefaultToolInput(BaseModel):


class NoopDefaultTool(BaseTool):
    name = "noop_default"
    description = "Tool for noOp default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the noOp default operation."""
        # Implement the tool logic here
        return f"Running noOp default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the noOp default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
