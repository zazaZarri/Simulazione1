class Sensore:
    
    def  __init__(self, codice: str, grandezza: int, misura: int, soglia_massima: int)
        self._codice = codice
        self._grandezza = grandezza
        self._misura = misura
        self._soglia_massima = soglia_massima
    
    @property
    def codice(self):
        return self._codice
    
    @property
    def grandezza(self):
        return self._grandezza
    
    @property
    def misura(self):
        return self._misura
    
    @property
    def soglia_massima(self):
        return self._soglia_massima
    
    @codice.setter
    def codice(self, x):
        _codice= x
    
    @grandezza.setter
    def grandezza(self,x):
        _grandezza= x
        
    @misura.setter
    def misura(self, x):
        _misura= x
        
    @soglia_massima.setter
    def soglia_massima (self,x):
        _soglia_massima= x
    