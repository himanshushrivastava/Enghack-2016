from trello import TrelloApi

trello = TrelloApi('a4ae903d87894a87ba4c6a7b7bf617bd')
token_url = trello.get_token_url('Trello Application', expires='30days', write_access=True)

print 'Navigate to the following webpage and click allow to recieve your Trello token'
print token_url
user_token = raw_input('Enter your token: ')

trello.set_token(user_token)
board_id = '576ec71a66056953359c2bcd'

board_information = trello.boards.get(board_id)
cards = trello.boards.get_card(board_id)
card_id_list = []

for card in cards:
    for key, value in card.items():
        print key, ": ", value
    card_id_list.append(card['id'])

for card_id in card_id_list:
    print trello.cards.get_field('name', card_id)