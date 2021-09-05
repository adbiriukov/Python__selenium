a = {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": "True",
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": "True"
}
print(a)
print(a['firstName'])
print(a['age'])
print(a['address']['streetAddress'])
print(a['address']['postalCode'])
print(a['phoneNumbers'][0]['number'])
print(a['phoneNumbers'][1]['number'])
print(a['children'])
print(a['spouse'])
