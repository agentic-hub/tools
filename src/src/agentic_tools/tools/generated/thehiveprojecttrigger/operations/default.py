from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class ThehiveprojecttriggerDefaultToolInput(BaseModel):
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    events: Optional[str] = Field(None, description="events")
    notice: Optional[str] = Field(None, description="You must set up the webhook in TheHive — instructions <a href=\"https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.thehive5trigger/#configure-a-webhook-in-thehive\" target=\"_blank\">here</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filter any incoming events based on their fields")


class ThehiveprojecttriggerDefaultTool(BaseTool):
    name = "thehiveprojecttrigger_default"
    description = "Tool for theHiveProjectTrigger default operation - default operation"
    
    def _run(self, **kwargs):
        """Run the theHiveProjectTrigger default operation."""
        # Implement the tool logic here
        return f"Running theHiveProjectTrigger default operation with args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the theHiveProjectTrigger default operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
