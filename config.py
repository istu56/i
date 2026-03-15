from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = int(getenv("OWNER_ID", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AloneUpdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AloneBotSupport")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "# Netscape HTTP Cookie File
# https://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file! Do not edit.

.youtube.com TRUE / TRUE 1788867891 __Secure-YNID 16.YT=jXXIt-xTri9Jwk9DNha_678Ft4296P7vD0IQxRwEyp_ET-3SnFF9e1ANpuiZYJ1sPVkc6TNJ_mEslK39tRHF3zIfarU0rzBV2T_wxl8FzsuX6MmFpuPNNj94v-FaGmK8UbrxOxeyuM8xz7Bh9F86vsdxFUa0DV1ccn8ojQasWYmPxC0i_iPYCsAU73AIVNGTK4Ih1ghOSDeLVvOa8-KqFUZ5quYz8bHgJL8V8jFWtbNH0i15TGLLJgfsQawS00P5A7SCWpdxjmZD-AXmgZysVmgBxjxXLqdifE9BQ30rAPwl6m8Ggdpa0YU7kdTVc7TWVsIgVnavBUJ0Mcoh-rRDrg
.youtube.com TRUE / TRUE 1773317692 GPS 1
.youtube.com TRUE / TRUE 1788868298 VISITOR_INFO1_LIVE NU94LsDPkQQ
.youtube.com TRUE / TRUE 1788868298 VISITOR_PRIVACY_METADATA CgJJThIEGgAgXA%3D%3D
.youtube.com TRUE / TRUE 1807876298 PREF f6=40000000&tz=Asia.Kolkata&f7=100&f4=4000000
.youtube.com TRUE / TRUE 1804851962 __Secure-1PSIDTS sidts-CjQBBj1CYhPasVxx4KP7Ig_Fyfd0MuAxjYHEYXGVBmAJEQh3jHRAjQfcAaDtAf_ZFkNqj0aAEAA
.youtube.com TRUE / TRUE 1804851962 __Secure-3PSIDTS sidts-CjQBBj1CYhPasVxx4KP7Ig_Fyfd0MuAxjYHEYXGVBmAJEQh3jHRAjQfcAaDtAf_ZFkNqj0aAEAA
.youtube.com TRUE / FALSE 1807875962 HSID A8IUD3feaRtaa71Hg
.youtube.com TRUE / TRUE 1807875962 SSID ApEeIVnaJOj4y8URR
.youtube.com TRUE / FALSE 1807875962 APISID MuSHIs33DkGDh8Vp/AAtC-CpMLbSEXZBIZ
.youtube.com TRUE / TRUE 1807875962 SAPISID rlApC99xMvoYJq4y/ACG8UTS_IHYpK4yVu
.youtube.com TRUE / TRUE 1807875962 __Secure-1PAPISID rlApC99xMvoYJq4y/ACG8UTS_IHYpK4yVu
.youtube.com TRUE / TRUE 1807875962 __Secure-3PAPISID rlApC99xMvoYJq4y/ACG8UTS_IHYpK4yVu
.youtube.com TRUE / FALSE 1807875962 SID g.a0007giIrcDyZEbi-Z9yygCCswBYlXi12S-CzJweO1ED49w5s-IuvNAbQfDbaLPYkiMya3ZRNQACgYKAcISARISFQHGX2MiD_SSq_DH-luJZwTyjYospRoVAUF8yKrkAJNdCJ02nriYsK8Anymg0076
.youtube.com TRUE / TRUE 1807875962 __Secure-1PSID g.a0007giIrcDyZEbi-Z9yygCCswBYlXi12S-CzJweO1ED49w5s-IuD9qihIuO2xhSvx35OiDLAgACgYKAakSARISFQHGX2MieOe-j8IUHw9YFYU2d7a23BoVAUF8yKqAoByBZ7wnaiTxrhuoLVBM0076
.youtube.com TRUE / TRUE 1807875962 __Secure-3PSID g.a0007giIrcDyZEbi-Z9yygCCswBYlXi12S-CzJweO1ED49w5s-Iu6vvr9ioi4xs9yNdsrFqEpAACgYKAccSARISFQHGX2MiDJHojbd_aTQfV_6mv1PjzBoVAUF8yKptcCbSGAcqJsAplm2_XHHw0076
.youtube.com TRUE / FALSE 1804852300 SIDCC AKEyXzVyHxG0d3EPS_UrahGQHiUmF3QXS0obE6mVgsiQD62L9uQ_6PmLBr1YgcLmsiS8S2qu
.youtube.com TRUE / TRUE 1804852300 __Secure-1PSIDCC AKEyXzUwPZTbNu97Ht0s-osntQQyRaNyQKVWl97dG01Rgn6BDGUHH5GTL5BrFrbKRQrI5Kui
.youtube.com TRUE / TRUE 1804852300 __Secure-3PSIDCC AKEyXzWP4COYqMY2mE_Id3NT8aOAK9HxaW4v1JarfpWEd8p-Jq8qRSmSdAnno1YF-3c7ZFnEcQ
.youtube.com TRUE / TRUE 1807876030 LOGIN_INFO AFmmF2swRQIgZrDSuyf5CYkSRJ28QCItGZiHKadbcvMjWWzLfN8LsLkCIQDxqMmKiNom0HqOLjBMGhqqrf72KNFL9PITggTN_FkvQQ:QUQ3MjNmeWRRUUJ1aE9Sdl9IbkpHWFlHcHJBaTNyUFdlaE1ZQ00ya2dVUHdkVUotS2I1ZG5wdVBxdHdOR3ROOEhWeVZqSnNfRlJyUDdaemZwXzJGd0NEX3Y4WXFfR3pqTHZMb2JadjlZTzlSQWxMNk5NYUN3YlJyZFByQ2E3NHFHZS1JMWlWRzBiYXdEOXlpSHViR3RPNEptWndRQm9USzl3
.youtube.com TRUE / FALSE 1773316099 ST-10gaeza csn=r77fVpaDmLhhx11w&itct=CGcQ_FoYASITCJeQyZylmpMDFaRjnQkdkp8BMTIGc2VhcmNoUgpoaW5kaSBzb25nmgEDEPQkygEEg1VGZg%3D%3D
.youtube.com TRUE / FALSE 1773316103 ST-5j6ket csn=r77fVpaDmLhhx11w&itct=CGMQ_FoYAyITCJeQyZylmpMDFaRjnQkdkp8BMTIGc2VhcmNoUgpoaW5kaSBzb25nmgEDEPQkygEEg1VGZg%3D%3D
.youtube.com TRUE / FALSE 1773316206 ST-1u41icc csn=B0HFAG_l1UibWAlI&itct=CKcBEPxaIhMI2YXJuqWakwMV7VadCR0y_BpVMgpnLWhpZ2gtcmVjWg9GRXdoYXRfdG9fd2F0Y2iaAQYQjh4YngHKAQSDVUZm
.youtube.com TRUE / FALSE 1773316294 ST-1d4lv26 csn=cNxbDi75wzCSQRnt&itct=CJgBEIf2BBgBIhMIqryX9qWakwMV0FWdCR2GRR_aWg9GRXdoYXRfdG9fd2F0Y2iaAQUIJBCOHsoBBINVRmY%3D
.youtube.com TRUE / TRUE 0 YSC 4EN926dOQwM").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
