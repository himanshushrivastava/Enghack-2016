from trello import TrelloApi
import webbrowser
import os

trello_report = open('trello_report.html', 'w')

trello = TrelloApi('a4ae903d87894a87ba4c6a7b7bf617bd')
token_url = trello.get_token_url('Trello Application', expires='30days', write_access=True)

user_name = raw_input('Enter user name: ')
print '\nNavigate to the following webpage and click "Allow" to receive your Trello token:\n'
print token_url
user_token = raw_input('\nEnter your token: ')

trello.set_token(user_token)

boards = trello.members.get_board(user_name)
print '\nThese are the boards available on your account:\n'
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

html = """
<html>
  <head></head>
  <body>
"""

for card_list in card_lists:
    html = html + '<p><strong>%s</strong></p>' % card_list['name']
    html = html + '<ul>'
    cards = trello.lists.get_card(card_list['id'])
    for card in cards:
        card_values = trello.cards.get_field('name', card['id'])
        html = html + '<li>%s</li>' % card_values['_value']
    html = html + '</ul>'

working_directory = os.getcwd()
working_directory = working_directory.replace('\\', '/')
trello_report_path = 'file://' + working_directory + '/trello_report.html'

trello_report.write(html)
trello_report.close()

webbrowser.open(trello_report_path, new=2)
