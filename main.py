from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import re
import unidecode

cursed_words = [
'arregassado',
'arrombado',
'babaca',
'baitola',
'biroska',
'bobo',
'bolagato',
'boqueteiro',
'buceta',
'bundao',
'cabaco',
'cacete',
'cadelona',
'caralho',
'cocozento',
'cu',
'debil mental',
'demente',
'desgracado',
'drogado',
'endemoniado',
'energumeno',
'enfianocu',
'engolerola',
'escroto',
'esporrado',
'estrume',
'fdp',
'fidumaegua',
'filho da puta',
'fiofo',
'foda',
'fuder',
'fudido',
'gordoescroto',
'kct',
'ku',
'lazarento',
'leproso',
'lezado',
'merda',
'mocorongo',
'montedemerda',
'n00b',
'nazista',
'newbie',
'olhodocu',
'otario',
'passaralho',
'pau no cu',
'piroca',
'porra',
'punheta',
'puta',
'pqp',
'quenga',
'rapariga',
'retardado',
'rusguento',
'tarado',
'tetuda',
'tetudo',
'troglodita',
'vadia',
'vagabundo',
'vagaranha',
'vai a merda',
'vsf',
'vai tomar no cu',
'vascaino',
'verme',
'xavasca',
'xereca',
'xixizento',
'xoxota',
'xupetinha',
'xupisco',
'xurupita',
'xuxexo',
'xxt',
'xxx',
'ze buceta',
'zebuceta'
]

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def detectCursedWord(message):
    found_words = list()
    words = message.split(' ')
    for word in (words):
        if(word.lower() in cursed_words):
            found_words.append(word)
    found_words = ', '.join(found_words)
    return found_words

def echo(bot, update):  
    unicode_message = u''+update.message.text
    print('fdafsadf')
    print(unidecode.unidecode(unicode_message))
    bad_words = detectCursedWord(unidecode.unidecode(unicode_message))
    if(bad_words):
        bot.send_message(chat_id=update.effective_chat.id, text='PALAVRÃO É FEIO')

def main():
    updater = Updater('1056534064:AAEwTEowk9eFOF7sT9FuyMfSO5T9wWWsjPw')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()
    return 'ok'

if __name__ == '__main__':
    main()