import os
from vars import CREDIT, OWNER
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Message
# .....,.....,.......,...,.......,....., .....,.....,.......,...,.......,.....,

# upgrade button
def register_upgrade_handlers(bot):
    @bot.on_callback_query(filters.regex("upgrade_command"))
    async def upgrade_button(client, callback_query):
      user_id = callback_query.from_user.id
      first_name = callback_query.from_user.first_name
      keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main_menu")]])
      caption = (
          f"🌟 <b>Welcome [{first_name}](tg://user?id={user_id}) in HG DRM Bot 🤖</b> 🌟\n\n"
          f"🔐 <b>Features You Unlock:</b>\n"
          f"━━━━━━━━━━━━━━━━━━━━━━\n"
          f"<blockquote>🎓 Classplus DRM / NDRM\n"
          f"🧑‍🏫 PhysicsWallah Login\n"
          f"📖 CareerWill (Brightcove & New)\n"
          f"🎓 Khan GS\n"
          f"🚀 APPX * Encrypted\n"
          f"🎥 VisionIAS (Old)\n"
          f"💻 Zoom | Utkarsh (Video + PDF)\n"
          f"🌐 Non-DRM + AES URLs\n"
          f"🔑 MPD Links (with valid key)</blockquote>\n"
          f"━━━━━━━━━━━━━━━━━━━━━━\n"
          f"💎 <b>Membership - 500 INR / Month</b>\n"
          f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
          f"📬 <b>Want to Join?</b>\n"
          f"💬 Contact ➡️ [{HG}](tg://user?id={OWNER}) to activate your access."
      )
    
      await callback_query.message.edit_media(
        InputMediaPhoto(
          media="https://freeimage.host/i/Kvo7UQt",
          caption=caption
        ),
        reply_markup=keyboard
   )
