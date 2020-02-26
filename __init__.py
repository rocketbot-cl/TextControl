# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import re

"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "filter":

  try:
      text = GetParams('text')
      ref1 = GetParams('ref1')
      ref2 = GetParams('ref2')
      var_ = GetParams('var_')

      print(text, ref1, ref2, var_)

      filter = re.search("" + ref1 + "(.+?)" + ref2 + "", text).group(1)

      SetVar(var_, filter)
  except:
      PrintException()
