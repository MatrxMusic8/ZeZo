from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","DarkxMusic")
BOT_USERNAME = getenv("BOT_USERNAME", "M_U_S_I_C_900_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "B_o_d_a_90")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "E_s_l_a_m_Zelzal")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/b557e5cffeadff7704af9.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8e9ba80daf4e08fe290e0.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5648157552").split()))
