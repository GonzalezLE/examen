from typing import List


class AnalyzeNumbers():
    def __init__(self, list_of_number:List[int]):
        self.list_of_number = list_of_number
    
    
    def is_par_or_impar(self):
        """Este método recorre la lista list_of_number que es la lista que pasamos al momento de crear la instancia de la clase AnalyzeNumbers:

                - Evalua si el numero es par o impar 
                - Manda a traer el metodo is_multiple_of_four para evalua que sea multiplo de 4
                
            -   Return
                Imprime por consola si el número es par o impar 

        """        
        for numero in self.list_of_number:
            
            # evaluo que sea par o impar
            if numero % 2 == 0:
                print(f'Numero {numero} es par')
            else:
                print(f'Numero {numero} es impar')
            
            # mando a traer metodo que evalua si es multiplo de 4
            if self.is_multiple_of_four(numero):
                print(f'Numero {numero} es multiplo de 4 \n')
            else:
                print(f'Numero {numero} no es multiplo de 4 \n')
    
    
    def is_multiple_of_four(self,numero:int):
        """Evalue si un numero es multiplo de 4

        Args:
            numero (int): Numero que se va a evaluar

        Returns:
            bool: True si es multiplo
                  False si no es multiplo
        """
        if numero % 4 == 0:
            return True
        else:
            return False



# test
if __name__ == "__main__":
    
    print("""
          *****************************************************************************
                Prueba numero 1 lista de numeros [10,6,8,-5,-89,90]
          *****************************************************************************
          """)
        
    case1:List[int] = [10,6,8,-5,-89,90]
    obj_analyze = AnalyzeNumbers(case1)
    obj_analyze.is_par_or_impar()
    
    print("""
          *****************************************************************************
                Prueba numero 1 lista de numeros [30,21,6,-30,-6,-21]
          *****************************************************************************
          """)
        
    case2:List[int] = [30,21,6,-30,-6,-21]
    obj_analyze = AnalyzeNumbers(case2)
    obj_analyze.is_par_or_impar()
    
    print("""
          *****************************************************************************
                Prueba numero 1 lista de numeros [-10]
          *****************************************************************************
          """)
    
    case3:List[int] = [-10]
    obj_analyze = AnalyzeNumbers(case3)
    obj_analyze.is_par_or_impar()



