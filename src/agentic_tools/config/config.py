import os


class Config:
    def __init__(self):
        self.agentichub_url = os.environ.get("AGENTICHUB_URL", "api.scade.pro/")
        self.api_token = os.environ.get("AGENTICHUB_API_TOKEN", "")
        # Ensure URL has proper format
        if not self.agentichub_url.startswith(("http://", "https://")):
            self.agentichub_url = f"https://{self.agentichub_url}"


config = Config()
