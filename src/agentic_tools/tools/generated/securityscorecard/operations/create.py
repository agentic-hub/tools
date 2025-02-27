from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SecurityscorecardCredentials

class SecurityscorecardCreateToolInput(BaseModel):
    description: Optional[str] = Field(None, description="Description")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    email: Optional[str] = Field(None, description="Email")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the portfolio")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    scorecard_identifier: Optional[str] = Field(None, description="Primary identifier of a company or scorecard, i.e. domain.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message for the invitee")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    portfolio_id: Optional[str] = Field(None, description="Portfolio ID")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    first_name: Optional[str] = Field(None, description="First Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    privacy: Optional[str] = Field(None, description="Privacy")


class SecurityscorecardCreateTool(BaseTool):
    name: str = "securityscorecard_create"
    connector_id: str = "nodes-base.securityScorecard"
    description: str = "Tool for securityScorecard create operation - create operation"
    args_schema: type[BaseModel] | None = SecurityscorecardCreateToolInput
    credentials: Optional[SecurityscorecardCredentials] = None
