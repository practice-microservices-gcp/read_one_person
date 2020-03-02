from controllers.search_id_controller import readOnePerson

response = readOnePerson('1')

print(f'Response code {response.code} and body {response.body.to_json()}')