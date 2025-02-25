from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwstranscribeDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    transcriptionJobName: Optional[str] = Field(None, description="The name of the job")
    operation: Optional[str] = Field(None, description="Operation")


class AwstranscribeDeleteTool(BaseTool):
    name = "awstranscribe_delete"
    description = "Tool for awsTranscribe delete operation - delete operation"
    
    def _run(self, **kwargs):
        """Run the awsTranscribe delete operation."""
        # Implement the tool logic here
        return f"Running awsTranscribe delete operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsTranscribe delete operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
