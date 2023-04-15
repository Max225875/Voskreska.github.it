library(telegram.bot)
library(stringr)
library(lgr)

# Включаем логгер
lg <- get_logger()
lg$set_appenders(AppenderFile$new(file = 'log/bot.log'))
lg$info('Bot start')

# Включаем параллельный план вычислений
lg$info('Run multisession mode')
future::plan('multisession', workers = 4)

# Инициализируем бота
lg$info('Make updater')
updater <-  Updater(bot_token('botname'))
# Очищаем очередь бота от старых сообщений
lg$info('Clean update queue')
updater$bot$clean_updates()

# Функция с длительным временем вычислений
slow_fun <- function(bot, update) {
  
  lg$info('Run slow command')
  # Запускаем выполнение кода в параллельной сессии
  promises::future_promise(
    {
      # Сообщение о том, что начата работа длительного вычисления
      bot$sendMessage(update$message$chat_id,
        text = str_glue("Медленная функция, начало работы!\nID процесса: {Sys.getpid()}"),
        parse_mode = "Markdown")
      
      # Добавляем паузу, для того, что бы искусственно сделать функцию длительной
      Sys.sleep(10)
      
      # Сообщаем о том, что все вычисления выполнены
      bot$sendMessage(update$message$chat_id,
        text = str_glue("Медленная функция выполнена!\nID процесса: {Sys.getpid()}"),
        parse_mode = "Markdown")
    }
  )
  
}

# Функция с коротким временем вычислений
fast_fun <- function(bot, update) {
  
  lg$info('Run fast command')
  # Просто отправляем сообщение
  bot$sendMessage(update$message$chat_id,
    text = str_glue("Быстрая функция, выполняется последовательный режим!\nID процесса: {Sys.getpid()}"),
    parse_mode = "Markdown")
  
}

# Остановка пуллинга
stop <- function(bot, update) {
  
  lg$info('Bot stop')
  bot$sendMessage(update$message$chat_id,
    text = str_glue("Останавливаю работу бота!\nID процесса: {Sys.getpid()}"),
    parse_mode = "Markdown")
  # Просто отправляем сообщение
  updater$stop_polling()
  
}

# Функция с ошибкой, имитирующая падение бота
crush <- function(bot, update) {
  
  lg$info('Crush command')
  bot$sendMessage(update$message$chat_id,
    text = str_glue("Функция с ошибкой, сбой в работе бота!\nID процесса: {Sys.getpid()}"),
    parse_mode = "Markdown")
  
  stop("Ошибка, сбой бота!")
  
}

# создаём обработчик
lg$info('Make handlers')
slow_hendler <- CommandHandler('slow', slow_fun)
fast_hendler <- CommandHandler('fast', fast_fun)
stop_hendler <- CommandHandler('stop', stop)
crush_hendler <- CommandHandler('crush', crush)

# добавляем в диспетчер
lg$info('Add handlers to dispatcher')
updater <- updater + slow_hendler + fast_hendler + stop_hendler + crush_hendler

# запускаем бота
lg$info('Run polling')
updater$start_polling()
