from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/termux_tools_AA")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/WH173_5P1D3R")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nIam YT Downloader Bot! [📥](https://t.me/WH173_5P1D3R)\nI'M YT DL Bot 🤖 By @WH173_5P1D3R\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
