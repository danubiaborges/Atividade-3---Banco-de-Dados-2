from view import View
from northwind_dao import orderDAO
from Models import models_northwind_driver


class Controller:
    def __init__(self):
        self.view = View()
        self.orderDAO = orderDAO()

    def start(self):
        option = self.view.start()

        while option != '6':

            if option == '1':           
                order = self.view.insert_order()
                try:
                    self.orderDAO.insert_order(order)
                    self.view.display_message("Inserido com sucesso") 
                except Exception as e:
                    error_message = "Erro na inserção. Detalhes: " + str(e)
                    self.view.display_message(error_message)


    
                
            elif option == '2':         #Informações completas sobre um pedido
                requestedOrder = self.view.get_order()
                result = self.orderDAO.search_order(requestedOrder)
                if result[2]:
                    registers = result[2]
                    self.view.display_information(registers)
                else:
                    self.view.display_message("Uma order com este ID não existe!") 

                
            elif option == '3':         #Ranking dos funcionários por intervalo de tempo
                result = self.orderDAO.get_employee_rank()
                if result[2]:
                    registers = result[2]
                    self.view.display_rank(registers)
                else:
                    self.view.display_message("Erro na busca") 
                

            elif option == '6':
                self.view.exit_program()
                return

            else:
                self.view.valid_entry()

            option = self.view.menu()


if __name__ == '__main__':
    main = Controller()
    main.start()
