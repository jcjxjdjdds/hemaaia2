from pyrogram import Client

api_id =  24514467
api_hash = '5a8c3d38c4d89b672062c5ff015380c7'
app = Client('sessions/aeoenzbxsx', api_id=api_id, api_hash=api_hash)
app.connect()

app.send_message('@O7_05, 'hello')

app.disconnect()