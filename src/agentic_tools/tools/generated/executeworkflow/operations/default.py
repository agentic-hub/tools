from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ExecuteworkflowDefaultToolInput(BaseModel):
    workflow_id: Optional[str] = Field(None, description="Note on using an expression here: if this node is set to run once with all items, they will all be sent to the <em>same</em> workflow. That workflow's ID will be calculated by evaluating the expression for the <strong>first input item</strong>.")
    source: Optional[str] = Field(None, description="Where to get the workflow to execute from")
    workflow_path: Optional[str] = Field(None, description="The path to local JSON workflow file to execute")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    mode: Optional[str] = Field(None, description="Mode")
    workflow_url: Optional[str] = Field(None, description="The URL from which to load the workflow from")
    execute_workflow_notice: Optional[str] = Field(None, description="Any data you pass into this node will be output by the Execute Workflow Trigger. <a href=\"https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow/\" target=\"_blank\">More info</a>")
    workflow_json: Optional[str] = Field(None, description="The workflow JSON code to execute")
    operation: Optional[str] = Field(None, description="Operation")


class ExecuteworkflowDefaultTool(BaseTool):
    name: str = "executeworkflow_default"
    description: str = "Tool for executeWorkflow default operation - default operation"
    args_schema: type[BaseModel] | None = ExecuteworkflowDefaultToolInput
