import Metashape


def check_license() -> None:
    if Metashape.app.activated:
        print("Metashape is activated: ", Metashape.app.activated)
    else:
        print("No licence found. Please check that you linked your license (floating or standalone) wih the Metashape python module.")
        exit()
