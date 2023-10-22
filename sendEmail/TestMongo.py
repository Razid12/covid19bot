from pymongo import MongoClient
client = MongoClient("mongodb+srv://covid_19:ikJDtQZYlZEtkWj5@cluster0.kjv30bd.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('covid19DB')
records = db.chat_records
print(records.count_documents({}))
new_chat = {
    'name': 'ram',
    'roll_no': 321,
    'branch': 'it'
}
result = records.delete_many({})
print(f"Deleted {result.deleted_count} documents.")





