"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_11():
     """
     Construya una tabla que contenga `c0` y una lista separada por ',' de
     los valores de la columna `c4` del archivo `tbl1.tsv`.

     Rta/
          c0       c4
     0     0    b,f,g
     1     1    a,c,f
     2     2  a,c,e,f
     3     3      a,b
     ...
     37   37  a,c,e,f
     38   38      d,e
     39   39    a,d,f
     """

     import pandas as pd

     df = pd.read_csv("files/input/tbl1.tsv", sep="\t")

     grouped = df.groupby("c0")

     result = pd.DataFrame()
     for name, group in grouped:
          sorted_values = sorted(group["c4"])
          joined_values = ",".join(str(value) for value in sorted_values)
          result.loc[name, "c0"] = name
          result.loc[name, "c4"] = joined_values
     print(result)
     return result