from pathlib import Path
import time

log_route = Path("./log.txt")


def write_log(newcontent={}):
    content = read_log()

    if content["status"] == 200 or content["status"] == 404:
        content[
            "txt"
        ] += f'[{newcontent["time"]}][{newcontent["user"]}][{newcontent["origin"]}][{newcontent["status"]}]\n'
        try:
            log_route.write_text(content["txt"])
            return {"txt": "", "msj": "Archivo actualizado correctamente.", "status": 200}
        except IOError as e:
            print(e)
            return {
                "txt": "",
                "msj": "Error al escribir el archivo",
                "status": 500,
                "error": e,
            }
    else:
        return content


def read_log():
    try:
        content = log_route.read_text()
        return {"txt": content, "msj": "", "status": 200}
    except FileNotFoundError as err:
        print(err)
        log_route.write_text(
            "** Estructura del log [HORA][USUARIO][ORIGEN][RESPUESTA] **\n\n"
        )
        return {
            "txt": "** Estructura del log [HORA][USUARIO][ORIGEN][RESPUESTA] **\n\n",
            "msj": "Archivo no encontrado",
            "status": 404,
        }
    except IOError as e:
        print(e)
        return {"txt": "", "msj": "Error al leer el archivo", "status": 500, "error": e}


# read_log()
# print(
#     write_log(
#         newcontent={
#             "user": "Naomi",
#             "time": int(time.time()),
#             "origin": "api",
#             "status": 200,
#         }
#     )
# )
