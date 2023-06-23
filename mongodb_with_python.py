import pymongo


client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']
information=mydb.employeeinformation


record = [{
    'firstname':'pankaj',
    'course':'BTCS',
    'age':22,
    'status':'single'
},
{
    'firstname':'ravi',
    'course':'BTCS',
    'age':21,
    'status':'mingle but divorced'
},
{
    'firstname':'amanuwell',
    'course':'BTCS',
    'age':22,
    'status':'always single'
},
{
    'firstname':'subash',
    'course':'BTCS',
    'age':20,
    'status':'broken'
}
]

information.insert_many(record)     #for single entry -- insert_one

# finding a single file which is at index 0
information.find_one()

print("\n-----------------------------------------------------------------------------")
# selecting the whole record  -- similar like Select * from database

for reord in information.find():
    print(record)


print("\n-----------------------------------------------------------------------------")

# reading the record which satisfies the condition just like -- Select * from database where condition=value     or row=data
for record in information.find({'firstname':'ravi'}):
    print(record)

print("\n-----------------------------------------------------------------------------")
# $in -- means OR operation if either the value will match, it reads the data

for record in information.find({'age': {'$in': ['22', '20']}}):
    print(record)


print("\n-----------------------------------------------------------------------------")

#AND operation
for record in information.find({'course':'BTCS','age':{'$lt':21}}):
    print(record)


# OR operation
for record in information.find({'$or':[{'firstname':'pankaj'},{'age':21}]}):
    print(record)


# AND operation
for record in information.find({'$and':[{'firstname':'pankaj'},{'age':22}]}):
    print(record)


inventory=mydb.inventory
inventory.insert_many([
{'book':'physics','quantity':25,'author':'pankaj'},
{'book':'chemistry','quantity':50,'author':'ravi'},
{'book':'maths','quantity':75,'author':'pankaj'},
{'book':'english','quantity':55,'author':'amanuwell'},
{'book':'socials','quantity':35,'author':'subash'}
]);


for record in inventory.find({'qty':{25,50,75}}):
    print(record)

