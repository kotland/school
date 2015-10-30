def search(data, **kwargs):
    pass

search([{},{}], name='Иван', surname='Иванов')
search([{},{}], surname='Иванов')

d = {'name': 'Иван'}

print(d.get('surname', True))