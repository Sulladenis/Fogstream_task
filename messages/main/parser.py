data = [
          {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            'list':['item1', 'item2' ],
            "address": {
              "street": "Victor Plains",
              "suite": "Suite 879",
              "city": "Wisokyburgh",
              "zipcode": "90566-7771",
              "geo": {
                "lat": "-43.9509",
                "lng": "-34.4618"
              }
            },
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
            "company": {
              "name": "Deckow-Crist",
              "catchPhrase": "Proactive didactic contingency",
              "bs": "synergize scalable supply-chains"
            }
          }
        ]

user_data = ""

#if data != None or isinstance(data, list):
#    data = data[0]

#for k, v in data.items():
#    if isinstance(v, list):
#        user_data = user_data + "{}:\n".format(k)
#    if isinstance(v, dict):
#        user_data = user_data + "{}:\n".format(k)
#        for k, v in v.items():
#            user_data = user_data + "    {}: {} \n".format(k, v)            
#    else:
#        user_data = user_data + "{}: {} \n".format(k, v)


def dispatch_list(data):
    if isinstance(data, list):
        print("я список ")   
        if not data:
            print("я пустой список")
        else:
            print("у меня есть вложения: ")
            iter_list(data)
    else:
        print("я не список, я:", data)


def dispatch_dict(data):
    if isinstance(data, dict):
        print("опа у нас тут словарик")
        if not data:
            print("я пустой словарик")
        else:
            print("я не пустой словарик")
            iter_dict(data)
    else:
        print('я не словарь я : ', data)


def iter_list(a):
    for i in a:
        dispatch_list(i)

def iter_dict(a):
    for i in a:
        dispatch_dict(a.get(i))

        
a = [14, 45, [12, 34]]
ad = {'a':[], "b": {"key": "valUe", "g": []}}
#iter_list(a)
iter_dict(ad)
#dispatcher(a)



#def get_from_list(data):
#    for v in data:

#        user_data = user_data + "{}:\n".format(v)

#def get_from_list(data):
#        for k, v in v.items():
#        user_data = user_data + "    {}: {} \n".format(k, v)
