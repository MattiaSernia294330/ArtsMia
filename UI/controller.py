import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._id_oggetto=None

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.numNodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.numEdges()} edges"))
        self._view._txtIdOggetto.disabled=False
        self._view._btnCompConnessa.disabled=False
        self._view.update_page()

    def handleCompConnessa(self,e):
        if self._id_oggetto is None:
            self._view.create_alert("Non hai inserito nulla, oppure quello che hai inserito non è un numero")
            return
        if not self._model.controllo(self._id_oggetto):
            self._view.create_alert("L'id inserito non si trova nel database")
            return
        componente_connessa=self._model.componente_connessa(self._id_oggetto)
        self._view.txt_result.controls.append(ft.Text(f"la componente connessa dell'opera con id {self._id_oggetto} ha {len(componente_connessa)+1} nodi"))
        self._view.update_page()

    def readId(self,e):
        value = e.control.value
        if value.strip().isdigit():
            self._id_oggetto = int(value)
        else:
            self._anno = None

