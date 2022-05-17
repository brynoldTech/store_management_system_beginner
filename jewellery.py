from Abstract_demo.base import Government


class Jewellery(Government):
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self):
        product_count = int(input(" \n Enter how many product want to add ? "))
        print("Enter your product list.. ")
        if self.product_list == []:
            for i in range(product_count):
                product = input()
                self.product_list.append(product)

            print("\n Your product has beed added to the list !")

        else:
            product = input()
            self.product_list.append(product)
            print("\n Your product has beed added to the list ! ")

    def view_product(self):
        print("List of your product..")
        for sl_no, product in enumerate(self.product_list, 1):
            print(f"{sl_no} {product}")

    def remove_product(self):
        print("\n Enter your product to remove form the list")
        product_name = input()
        if product_name in self.product_list:
            self.product_list.remove(product_name)
            print("\nYour product has been removed from the list..")

        else:
            print("\nYour product is not found in the list , please check the input ")


product_list = []
object_2 = Jewellery(product_list)

while True:
    print("1.Add product ")
    print("2.View product")
    print("3. Remove product ")
    print("4 Quit")
    data = int(input("\n Please select your option "))
    if data == 1:
        object_2.add_product()
    elif data == 2:
        object_2.view_product()
    elif data == 3:
        object_2.remove_product()
    else:
        """ inbuild function"""
        quit()
