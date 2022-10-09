
import FreeCAD
import ImportGui
import Mesh

def closeDocs():
    documentList = App.listDocuments()

    for doc in documentList:
        App.closeDocument(doc)

def process_item(filename):
    closeDocs()
    ImportGui.open(filename + '.step')
    Gui.Selection.addSelection("Unnamed", 'Solid')
    obj = Gui.Selection.getSelection()
    Mesh.export(obj, filename + '_freecad.stl')

files = [ "/Users/david/Documents/dactyl-keyboard/david/_5x6_NONE_right","/Users/david/Documents/dactyl-keyboard/david/_5x6_NONE_left","/Users/david/Documents/dactyl-keyboard/david/_5x6_NONE_right_plate","/Users/david/Documents/dactyl-keyboard/david/_5x6_NONE_left_plate" ]

documentList = App.listDocuments()

for doc in documentList:
    App.closeDocument(doc)


for file in files:
    try:
        process_item(file)
    except Exception as err:
        print(f"Error {err=}, {type(err)=}")


print('Done')
