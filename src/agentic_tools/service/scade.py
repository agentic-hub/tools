import typing
import aiohttp
from pydantic import BaseModel
import requests
from agentic_tools.config import config


class ScadeService:
    def __init__(self):
        self.agentichub_url = config.agentichub_url
        self.api_token = config.api_token

    def execute_connector(
        self,
        connector_id: str,
        credentials: typing.Optional[BaseModel] = None,
        data: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Dict[str, typing.Any]:
        """Execute a connector synchronously using requests."""
        url = f"{self.agentichub_url}api/v1/scade/connector/execute"

        headers = {"Authorization": self.api_token, "Content-Type": "application/json"}

        payload = {
            "connector_id": connector_id,
            "credentials": credentials.model_dump() or {} if credentials else {},
            "data": data or {},
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(
                f"Error executing connector: {response.status_code} - {response.text}"
            )

        return response.json()

    async def aexecute_connector(
        self,
        connector_id: str,
        credentials: typing.Optional[typing.Dict[str, typing.Any]] = None,
        data: typing.Optional[typing.Dict[str, typing.Any]] = None,
    ) -> typing.Dict[str, typing.Any]:
        """Execute a connector asynchronously using aiohttp."""
        url = f"{self.agentichub_url}api/v1/scade/connector/execute"

        headers = {"Authorization": self.api_token, "Content-Type": "application/json"}

        payload = {
            "connector_id": connector_id,
            "credentials": credentials or {},
            "data": data or {},
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(
                        f"Error executing connector: {response.status} - {error_text}"
                    )

                return await response.json()


scade_service = ScadeService()
