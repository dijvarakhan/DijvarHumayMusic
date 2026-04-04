# @The_Team_kumsal tarafından yasal olarak geliştirildi keyifli kullanımlar #kumsalteam
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "39221561"))
        self.API_HASH = getenv("API_HASH", "f450c818f9453c938e624fbdcb904998")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "7318798866:AAGJ4ZIsHSFKyjOTt2JSEwRc__JvqxJ1rT8")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://mongoguess:guessmongo@cluster0.zcwklzz.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003837773958"))
        self.OWNER_ID = int(getenv("OWNER_ID", "7612545925"))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 180)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 50))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "BAH8sMMASRl0kuwMlEr1qaJCX7HhxhyEpBUl8As7fWll71uhyxypW9LbTOo1EcXTevH8JU0jOxSfjC86M9Hi39G0mydufWLkFJkewYY1tKGpMd67rMjDx3goQXjso7cB6hjJHzhwypADMUlHQnZ4z1RIGzaAPa35UdnTGI_F_kL2HnT5bTLEm0CMgHPD12_jGf6Y7gtaVbez3fstfm7zAtIpRj3vF67rqvLklXSu62c1OA-SeGh2w2fl6wPs0Do9nqogrvidjKaH1d1cJRfJLRkZmmE9ZVKWTlZBQLp0lcZdhwftL8DyydFh7QkKahSIjxCEozLADq6JGlwZKYGmHKtFeoQcxQAAAAIMGeqQAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/humayliste")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/humayliste")

        def parse_bool(key: str, default: bool) -> bool:
            val = getenv(key)
            if val is None:
                return default
            return str(val).lower() in ["true", "1", "yes"]

        self.AUTO_END: bool = parse_bool("AUTO_END", False)
        self.AUTO_LEAVE: bool = parse_bool("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = parse_bool("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/unshepherding").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", self.DEFAULT_THUMB) or self.DEFAULT_THUMB
        self.START_IMG = getenv("START_IMG", self.DEFAULT_THUMB) or self.DEFAULT_THUMB

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
