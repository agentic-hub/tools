from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExecutiondataSaveToolInput(BaseModel):
    data_to_save: Optional[Dict[str, Any]] = Field(None, description="Data to Save")
    notice: Optional[str] = Field(None, description="Use this node to save fields you want to use later to easily find an execution (e.g. a user ID). You'll be able to search by this data in the 'executions' tab.<br>This feature is available on our Pro and Enterprise plans. <a href='https://n8n.io/pricing/' target='_blank'>More Info</a>.")
    operation: Optional[str] = Field(None, description="Operation")


class ExecutiondataSaveTool(BaseTool):
    name: str = "executiondata_save"
    description: str = "Tool for executionData save operation - save operation"
    args_schema: type[BaseModel] | None = ExecutiondataSaveToolInput
