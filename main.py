from trello import TrelloApi

trello = TrelloApi('a4ae903d87894a87ba4c6a7b7bf617bd')
token_url = trello.get_token_url('Trello Application', expires='30days', write_access=True)

user_name = raw_input('Enter user name: ')
print 'Navigate to the following webpage and click "Allow" to receive your Trello token'
print token_url
user_token = raw_input('Enter your token: ')

trello.set_token(user_token)

boards = trello.members.get_board(user_name)
print "\nThese are the boards available on your account:\n"
for board in boards:
    for key, value in board.items():
        if key == 'name':
            print value

board_name = raw_input('\nEnter the board for which you want generate a report: ')

for board in boards:
    for key, value in board.items():
        if key == 'name' and value == board_name:
            board_id = board['id']


board = trello.boards.get(board_id)
card_lists = trello.boards.get_list(board_id)

for card_list in card_lists:
    # for key, value in card_list.items():
    #     print key, ": ", value
    print ""
    print card_list['name']
    print ""
    cards = trello.lists.get_card(card_list['id'])
    for card in cards:
        card_values = trello.cards.get_field('name', card['id'])
        print card_values['_value']
