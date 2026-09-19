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
            [InlineKeyboardButton
