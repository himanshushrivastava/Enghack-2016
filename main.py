from trello import TrelloApi

trello = TrelloApi('a4ae903d87894a87ba4c6a7b7bf617bd')
token_url = trello.get_token_url('Trello Application', expires='30days', write_access=True)

print 'Navigate to the following webpage and click allow to recieve your Trello token'
print token_url
user_token = raw_input('Enter your token: ')

trello.set_token(user_token)
