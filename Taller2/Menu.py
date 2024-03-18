class Menu: #O(n)

    def orden(): #O(1)
        question = [
            inquirer.List('respuesta',
                        message="¿Importa el orden?",
                        choices=['Sí', 'No'],
                    ),
        ]  # O(1) 
