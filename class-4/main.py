# def main():
#     print("Hello from gh-class-4!")


# main()

# count = 1
   
# while count <= 3:
#     print("Kacha papita paka papita")
#     count += 1 

# iftar_items: list = ["Khujoor","Samosay", "Pakoray", "Rooh Afza", "Chana chaat" ]


# for items in iftar_items:
#     print(items)


def items(*n):
    sum = 0
    for item in n:
        sum += item
    print(sum)

items(2, 2, 5,6 , 7, 2, 2)

