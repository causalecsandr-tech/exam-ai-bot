            import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


def main_menu():
    keyboard = [
        [InlineKeyboardButton("📝 Задать вопрос", callback_data="question")],
        [InlineKeyboardButton("🎓 НМТ", callback_data="nmt")],
        [InlineKeyboardButton("📚 Подготовка к экзамену", callback_data="exam")],
        [InlineKeyboardButton("📖 Объяснить тему", callback_data="explain")],
        [InlineKeyboardButton("📝 Решить задание", callback_data="solve")],
        [InlineKeyboardButton("🔍 Проверить работу", callback_data="check")],
        [InlineKeyboardButton("❌ Мои ошибки", callback_data="mistakes")],
        [InlineKeyboardButton("📊 Мой прогресс", callback_data="progress")],
        [InlineKeyboardButton("🌐 Язык", callback_data="language")],
        [InlineKeyboardButton("⚙️ Настройки", callback_data="settings")],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет!\n\n"
        "Я ExamAI — помощник для учёбы и подготовки к НМТ.\n\n"
        "Выбери, что тебе нужно:",
        reply_markup=main_menu(),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "nmt":
        keyboard = [
            [InlineKeyboardButton("🇺🇦 Украинский язык", callback_data="ukrainian")],
            [InlineKeyboardButton("➗ Математика", callback_data="math")],
            [InlineKeyboardButton("📜 История Украины", callback_data="history")],
            [InlineKeyboardButton("🇬🇧 Иностранный язык", callback_data="foreign")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="menu")],
        ]

        await query.edit_message_text(
            "🎓 НМТ\n\nВыбери предмет:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data in ["ukrainian", "math", "history", "foreign"]:
        subjects = {
            "ukrainian": "🇺🇦 Украинский язык",
            "math": "➗ Математика",
            "history": "📜 История Украины",
            "foreign": "🇬🇧 Иностранный язык",
        }

        keyboard = [
            [InlineKeyboardButton("🎯 Начать тренировку", callback_data="training")],
            [InlineKeyboardButton("📝 Тест", callback_data="test")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="nmt")],
        ]

        await query.edit_message_text(
            f"{subjects[query.data]}\n\nВыбери режим:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "menu":
        await query.edit_message_text(
            "🏠 Главное меню",
            reply_markup=main_menu(),
        )

    elif query.data == "question":
        await query.edit_message_text(
            "📝 Задай мне вопрос сообщением.\n\n"
            "Например:\n"
            "«Объясни теорему Пифагора простыми словами»"
        )

    elif query.data == "explain":
        await query.edit_message_text(
            "📖 Напиши тему, которую нужно объяснить.\n\n"
            "Например: «Квадратные уравнения»."
        )

    elif query.data == "solve":
        await query.edit_message_text(
            "📝 Отправь условие задания текстом.\n\n"
            "Позже мы добавим возможность отправлять фотографии заданий."
        )

    elif query.data == "check":
        await query.edit_message_text(
            "🔍 Отправь свой ответ, и я помогу его проверить."
        )

    elif query.data == "mistakes":
        await query.edit_message_text(
            "❌ Здесь будут сохраняться твои ошибки."
        )

    elif query.data == "progress":
        await query.edit_message_text(
            "📊 Твой прогресс\n\n"
            "Пока статистики нет.\n"
            "После прохождения тестов здесь появятся результаты."
        )

    elif query.data == "language":
        keyboard = [
            [InlineKeyboardButton("🇺🇦 Українська", callback_data="lang_ua")],
            [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru")],
            [InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")],
            [InlineKeyboardButton("⬅️ Назад", callback_data="menu")],
        ]

        await query.edit_message_text(
            "🌐 Выбери язык:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ Настройки\n\n"
            "Здесь позже появятся настройки профиля, языка и уведомлений."
        )

    elif query.data in ["exam", "training", "test"]:
        await query.edit_message_text(
            "🚧 Этот раздел сейчас разрабатывается.\n\n"
            "Следующим этапом подключим реальные задания, тесты и ИИ."
        )

    elif query.data.startswith("lang_"):
        await query.edit_message_text(
            "✅ Язык сохранён.\n\n"
            "Возвращаемся в главное меню:",
            reply_markup=main_menu(),
        )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я получил твоё сообщение 👍\n\n"
        "ИИ пока не подключён. Следующим этапом подключим AI-модель, "
        "чтобы я мог отвечать на вопросы, объяснять темы и решать задания."
    )


def run():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не найден")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    print("ExamAI запущен!")
    app.run_polling()


if __name__ == "__main__":
    run()
