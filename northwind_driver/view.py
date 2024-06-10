import os


class View:

    def start(self):
        return self.menu()

    def menu(self):
        print('MENU')
        print('1. Inserir novo pedido')
        print('2. Informações completas sobre um pedido')
        print('3. Ranking dos funcionários por intervalo de tempo')
        print('6. Sair')
        option = input('Digite a opção: ')
        return option

    def insert_order(self):
        print('Incluir dados do pedido:\n')
        
        orderid = input('Digite o id do pedido: ')
        customerid = input('Digite o id do cliente: ')
        employeeid = input('Digite o nome do empregado: ')
        orderdate = input('Digite a data do pedido: ')
        requireddate = input('Digite a data necessária: ')
        shippeddate = input('Digite a data de envio: ')
        freight = input('Digite o freight: ')
        shipname = input('Digite o nome da entrega: ')
        shipaddress = input('Digite o endereço de entrega: ')
        shipcity = input('Digite a cidade de entrega: ')
        shipregion = input('Digite a região de entrega: ')
        shippostalcode = input('Digite o código postal: ')
        shipcountry = input('Digite o nome do país: ')
        shipperid = input('Digite o ID da transportadora: ')

        num_details = int(input("Quantos detalhes do pedido você deseja adicionar? "))
        order_details = []
        for _ in range(num_details):
            productid = input("Digite o Product ID: ")
            unitprice = input("Digite o Unit Price: ")
            quantity = input("Digite a Quantity: ")
            discount = input("Digite o Discount: ")
            order_details.append((orderid, productid, unitprice, quantity, discount))

        return {'order': [orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid], 'order_details': order_details}


    def get_order(self):
        orderid = input('Digite o id do pedido: ')
        return orderid


    def display_information(self, registers):
        print("Order Information:")
        for row in registers:
            print("------------------------")
            print("Order ID:", row[0])
            print("Order Date:", row[1])
            print("Customer Name:", row[2])
            print("Employee Name:", row[3])
            print("Product ID:", row[4])
            print("Unit Price:", row[5])
            print("Quantity:", row[6])
            

        input('\nPressione ENTER para sair.')
        
    def display_rank(self, registers):
        i = 1
        for row in registers:
            print("------------------------")
            print("Rank:", i)
            print("Firstname:", row[0])
            print("Hire Date:", row[1])
            print("Number of Orders:", row[2])
            print("Total Sales:", row[3])
            i = i + 1
            
        input('\nPressione ENTER para sair.')

    def display_message(self, message):
        print(message)
        input('\nPressione ENTER para sair.')

    def valid_entry(self):
        '''
        Entrada do MENU inválida
        '''


        print('Por favor, insira um valor válido.')
        input('\nPressione ENTER para retornar ao menu inicial.')

    def exit_program(self):
        os.system('clear')



