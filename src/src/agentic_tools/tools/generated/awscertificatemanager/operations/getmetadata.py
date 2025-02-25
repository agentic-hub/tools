from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class AwscertificatemanagerGetmetadataToolInput(BaseModel):
    certificateArn: Optional[str] = Field(None, description="String that contains the ARN of the ACM certificate to be renewed. This must be of the form: arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class AwscertificatemanagerGetmetadataTool(BaseTool):
    name = "awscertificatemanager_getmetadata"
    description = "Tool for awsCertificateManager getMetadata operation - getMetadata operation"
    
    def _run(self, **kwargs):
        """Run the awsCertificateManager getMetadata operation."""
        # Implement the tool logic here
        return f"Running awsCertificateManager getMetadata operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the awsCertificateManager getMetadata operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
