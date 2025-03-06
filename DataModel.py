from pydantic import BaseModel

class DataModel(BaseModel):
   
# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    
    u: float
    g: float
    i: float
    clase: object
    #.. COMPLETAR CON LAS VARIABLES EXPLICATIVAS DE LOS DATOS DEL LABORATORIO 1

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ['u', 'g', 'i','class']