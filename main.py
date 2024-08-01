
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()
secret = os.getenv('TOKEN')
users = ['brunoomf']
   
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Substitua 'YOUR_TOKEN' pelo token fornecido pelo BotFather

# Função de resposta a mensagens de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text.strip().lower()
    chat_data = context.user_data

    # Verifica se a primeira mensagem foi recebida
    if not chat_data.get('initial_message_received', False):
        response = "Olá! Como posso ajudar?"
        chat_data['initial_message_received'] = True
        chat_data['chat_active'] = True
    else:
        if user_message == "sim":
            response = "Obrigado por confirmar!"
            chat_data['chat_active'] = False  # Encerra o chat após a confirmação
        else:
            response = "Por favor, responda com 'sim' para continuar. Caso contrário, a conversa será reiniciada."
            # Retorna ao início, enviando a mensagem inicial novamente
            chat_data['initial_message_received'] = False

    # Envia a resposta ao usuário
    await update.message.reply_text(response)

def main() -> None:
    # Cria a aplicação e passa o token do bot
    application = Application.builder().token(secret).build()

    # Mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Inicia o bot
    application.run_polling()

if __name__ == '__main__':
    main()

