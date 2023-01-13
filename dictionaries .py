#keys have to be unique and immutable
#keys:values pairs are enclosed in {}
#note that empty brackets represent dictionies
#dictionaries are mutable
#-add new key:values pairs,
#-change the pairing
#-delete a key
capital={"India":"Delhi","USA":"WDC","France":"Paris","Sri Lanka":"Colombo"}
print(capital["India"])
print(capital.get("UK","Unknown"))#use of default value with get
capital["uk"]="london"#adds a new key:value
print(capital["uk"])
print(capital.keys())#gives all the keys
print(capital.values())#gives all the values
print(len(capital))
print("USA" in capital)
del capital["USA"]
print(capital)

countries=[]
for k in capital:
    countries.append(k)

countries.sort()
print(countries)

#CONSTRUCTIOPN OF AIRPORT
airports=dict([("mumbai","mom"),("delhi","del"),("chennai","maa")])
print(airports)

#DICTIONARY COMPREHENSION
sq={x:x*x for x in range(1,5)}
print(sq)

calories = dict([('burger',325), ('pizza' , 375), ('fries', 275), ('milk', 125)])
print(calories['burger'] + calories['milk'])
