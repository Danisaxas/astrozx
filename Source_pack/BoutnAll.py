from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_startbont = InlineKeyboardMarkup([[InlineKeyboardButton("𝗥𝗚𝗼𝗼𝗱 𝗠𝗫 ",url="wwww.pornhub.com"),
                                    InlineKeyboardButton("𝗺𝗮𝘅 ريكس 🇮🇳",url="t.me/Rexawait"),]])

_cmdsbont = InlineKeyboardMarkup([[InlineKeyboardButton("Gaterways",callback_data="gaters"),InlineKeyboardButton("Tools",callback_data="tools")],
                                  [InlineKeyboardButton("Closed",callback_data="closed")]])

_cmdsbontGater = InlineKeyboardMarkup([[InlineKeyboardButton("Free",callback_data="freegates"),
                                        InlineKeyboardButton("Premium",callback_data="premiumgates")],
                                        [InlineKeyboardButton("Return ",callback_data="rrtolls"),
                                        InlineKeyboardButton("Closed",callback_data="closed")]])

_cmdsbontTools  = InlineKeyboardMarkup([[InlineKeyboardButton("Next PAge ",callback_data="nettools")],[InlineKeyboardButton("Return ",callback_data="rrtolls"),InlineKeyboardButton("closed",callback_data="closed"),]])

_cmdsretbontgates  = InlineKeyboardMarkup([[InlineKeyboardButton("Return ",callback_data="gatesa"),InlineKeyboardButton("closed",callback_data="closed"),]])

_cmdsretbontgat  = InlineKeyboardMarkup([[InlineKeyboardButton("Return ",callback_data="nenor"),InlineKeyboardButton("closed",callback_data="closed"),]])


_registerDb  = InlineKeyboardMarkup([[InlineKeyboardButton("𝗔𝗰𝗲𝗽𝘁𝗮𝗿 ❇️",callback_data="acepconde"),InlineKeyboardButton("𝗥𝗲𝗰𝗵𝗮𝗿𝘇𝗮𝗿 🚫",callback_data="closed"),]])

def _infouser(
        name:str = None,
        usern:str = None,
        ):
    
    nix = InlineKeyboardMarkup([[InlineKeyboardButton(f"🤍", callback_data="corazon")],[InlineKeyboardButton(f"{name}",url=f"t.me/{usern}")]])
    return nix



selecidioma  = InlineKeyboardMarkup([[InlineKeyboardButton(" Español 🇪🇸",callback_data='es'),InlineKeyboardButton(" English 🇺🇸",callback_data='en')],[InlineKeyboardButton(" Arabic  🇸🇦",callback_data='sa'),InlineKeyboardButton(" China 🇨🇳",callback_data='cn')],[InlineKeyboardButton("France 🇫🇷",callback_data='fr'),InlineKeyboardButton("Vietnam 🇻🇳",callback_data='vn')],[InlineKeyboardButton("❗️ Exit ❗️",callback_data='closed'),]])

idiomatra = InlineKeyboardMarkup([[InlineKeyboardButton("! New idioma ¡",callback_data="otroidi"),InlineKeyboardButton("❗️ Exit ❗️",callback_data='closed'),]])

regene = InlineKeyboardMarkup([[InlineKeyboardButton("Regenerar 🌨",callback_data="regen")]])

def binchk(
        bin
        ):
    
    nix = InlineKeyboardMarkup([[InlineKeyboardButton(f"! Bin {bin} ¡", callback_data="binchk")]])
    return nix