import telebot
from datetime import datetime, timedelta

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'

bot = telebot.TeleBot(token=API_KEY)

orders = dict()
orders_values = dict()
order_date = dict()

price_dict = {
    'MC Rodeio Duplo': 25,
    'Whopper Lanche Feliz': 36,
    'Mega Quarteirão Staker 3.0': 45,
    'MC BK Original': 52,
    'Batata Frita': 10,
    'Onion Rings': 12,
    'Refrigerante': 8
}

def add_order(chatId, item, value):
    if chatId not in orders:
        orders[chatId] = {}
    
    if chatId not in orders_values:
        orders_values[chatId] = 0

    if item not in orders[chatId]:
        orders[chatId][item] = 0

    orders[chatId][item] += 1 
    orders_values[chatId] += value

def finish_order(chatId):
    if chatId not in order_date:
        order_date[chatId] = {}

    order_date[chatId]['date'] = datetime.now()
    order_date[chatId]['delivery'] = datetime.now() + timedelta(hours=1)

def delivery_or_cancel_confirm(chatId):
    del orders[chatId]
    del orders_values[chatId]
    del order_date[chatId]

def order_items_format(chatId):
    order = orders[chatId]
    order_items = ''
    for item in order:
        order_items += f'R$ {price_dict[item] * orders[chatId][item]} .... {orders[chatId][item]}x {item}\n'
    return order_items

''' Cardápio '''
@bot.message_handler(commands=['novo_pedido'])
def novo_pedido(message):
    if message.chat.id in orders:
        if orders_values[message.chat.id] > 0:
            text = f"""
                Você já possui um pedido em andamento!

Ele atualmente esta no valor de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para adicionar um item ao seu pedido
            """
            bot.send_message(message.chat.id, text)
            return

    text = """
        Olá, seja bem vindo à central de pedidos do BkDonalds!

Cardápio:

-> MC Rodeio Duplo - R$ 25,00
-> Whopper Lanche Feliz - R$ 36,00
-> Mega Quarteirão Staker 3.0 - R$ 45,00
-> MC BK Original - R$ 52,00
-> Batata Frita - R$ 10,00
-> Onion Rings - R$ 12,00
-> Refrigerante - R$ 8,00

Digite /mc_rod_duplo para pedir um MC Rodeio Duplo
Digite /whopper_feliz para pedir um Whopper Lanche Feliz
Digite /mega_quarteirao para pedir um Mega Quarteirão Staker 3.0
Digite /mc_bk_original para pedir um MC BK Original
Digite /batata_frita para pedir uma Batata Frita
Digite /onion_rings para pedir um Onion Rings
Digite /refrigerante para pedir um Refrigerante

Digite /menu caso não deseje iniciar um novo pedido
    """
    bot.send_message(message.chat.id, text)

''' Adicionar item ao pedido '''
@bot.message_handler(commands=['adicionar_item_pedido'])
def adicionar_item_pedido(message):
    text = """
        Olá, seja bem vindo à central de pedidos do BkDonalds!

Cardápio:

-> MC Rodeio Duplo - R$ 25,00
-> Whopper Lanche Feliz - R$ 36,00
-> Mega Quarteirão Staker 3.0 - R$ 45,00
-> MC BK Original - R$ 52,00
-> Batata Frita - R$ 10,00
-> Onion Rings - R$ 12,00
-> Refrigerante - R$ 8,00

Digite /mc_rod_duplo para pedir um MC Rodeio Duplo
Digite /whopper_feliz para pedir um Whopper Lanche Feliz
Digite /mega_quarteirao para pedir um Mega Quarteirão Staker 3.0
Digite /mc_bk_original para pedir um MC BK Original
Digite /batata_frita para pedir uma Batata Frita
Digite /onion_rings para pedir um Onion Rings
Digite /refrigerante para pedir um Refrigerante

Digite /finalizar para finalizar seu pedido
Digite /menu caso não vá finalizar seu pedido agora
    """
    bot.send_message(message.chat.id, text)

''' Itens do cardápio '''
@bot.message_handler(commands=['mc_rod_duplo'])
def mc_rod_duplo(message):
    add_order(message.chat.id, 'MC Rodeio Duplo', 25)
    
    text = f"""
        Você pediu um MC Rodeio Duplo!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['whopper_feliz'])
def whopper_feliz(message):
    add_order(message.chat.id, 'Whopper Lanche Feliz', 36)
    
    text = f"""
        Você pediu um Whopper Lanche Feliz!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['mega_quarteirao'])
def mega_quarteirao(message):
    add_order(message.chat.id, 'Mega Quarteirão Staker 3.0', 45)
    
    text = f"""
        Você pediu um Mega Quarteirão Staker 3.0!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['mc_bk_original'])
def mc_bk_original(message):
    add_order(message.chat.id, 'MC BK Original', 52)
    
    text = f"""
        Você pediu um MC BK Original!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['batata_frita'])
def batata_frita(message):
    add_order(message.chat.id, 'Batata Frita', 10)
    
    text = f"""
        Você pediu uma Batata Frita!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['onion_rings'])
def onion_rings(message):
    add_order(message.chat.id, 'Onion Rings', 12)
    
    text = f"""
        Você pediu um Onion Rings!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['refrigerante'])
def refrigerante(message):
    add_order(message.chat.id, 'Refrigerante', 8)
    
    text = f"""
        Você pediu um Refrigerante!

O valor total do seu pedido é de R$ {orders_values[message.chat.id]}

Digite /finalizar para finalizar seu pedido
Digite /adicionar_item_pedido para pedir outro item
    """

    bot.send_message(message.chat.id, text)

''' Finalizar pedido '''
@bot.message_handler(commands=['finalizar'])
def finalizar(message):
    text = f"""
        Seu pedido foi finalizado!

Digite /status_pedido para acompanhar o status do seu pedido
Digite /menu para acessar as demais opções
    """

    finish_order(message.chat.id)

    bot.send_message(message.chat.id, text)
''' ------------------------------------------------------------------------ '''

''' Status do pedido '''
@bot.message_handler(commands=['status_pedido'])
def status_pedido(message):
    if message.chat.id not in orders:
        text = """
            Você ainda não realizou nenhum pedido!
            
Digite /menu para acessar as opções disponíveis
        """
        bot.send_message(message.chat.id, text)
        return

    items = order_items_format(message.chat.id)

    text = f"""
        Seu pedido está sendo preparado!

Horário do pedido: {order_date[message.chat.id]['date'].strftime('%d/%m/%Y %H:%M:%S')}
Previsão de entrega: {order_date[message.chat.id]['delivery'].strftime('%d/%m/%Y %H:%M:%S')}

{items}

Total do pedido: R$ {orders_values[message.chat.id]}

Digite /cancelar_pedido para cancelar seu pedido
Digite /menu para acessar as demais opções
    """

    bot.send_message(message.chat.id, text)

''' Cancelar pedido '''
@bot.message_handler(commands=['cancelar_pedido'])
def cancelar_pedido(message):
    if message.chat.id not in orders:
        text = """
            Você ainda não realizou nenhum pedido!

Digite /menu para acessar as opções disponíveis
        """
        bot.send_message(message.chat.id, text)
        return

    delivery_or_cancel_confirm(message.chat.id)

    text = f"""
        Ahhh, que pena! Você cancelou seu pedido...

Digite /novo_pedido para iniciar um novo pedido
Digite /menu para acessar as demais opções
    """

    bot.send_message(message.chat.id, text)

''' Cancelar pedido '''
@bot.message_handler(commands=['confirmar_entrega'])
def confirmar_entrega(message):
    if message.chat.id not in orders:
        text = """
            Você ainda não realizou nenhum pedido!

Digite /menu para acessar as opções disponíveis
        """
        bot.send_message(message.chat.id, text)
        return

    delivery_or_cancel_confirm(message.chat.id)

    text = f"""
        Obrigado por confirmar o recebimento!

Estamos sempre à disposição para atendê-lo!

Digite /novo_pedido para iniciar um novo pedido
Digite /menu para acessar as demais opções
    """

    bot.send_message(message.chat.id, text)

def verify_message(message):
    return True

@bot.message_handler(func=verify_message)
def response(message):
    text = """
     🍔 Olá, seja bem-vindo ao nosso bot de pedidos do BK Donalds 🍟

Para que entre escolher entre Burguer King e MC Donalds ? Aqui você encontra os dois em um só lugar!

Atendemos em todo o Brasil, das 10h às 22h, de segunda a segunda, de terça a domingo. Faça agora seu pedido!

Digite /novo_pedido para iniciar um novo pedido.
Digite /status_pedido para verificar o status do seu pedido.
Digite /cancelar_pedido para cancelar o seu pedido.
Digite /confirmar_entrega para confirmar a entrega do seu pedido.
    """
    bot.send_message(message.chat.id, text)

bot.polling()

print('Bot is running...')