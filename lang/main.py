from os import path

def resolveMain():
    f_path = path.dirname(path.dirname(path.realpath(__file__))) + "\\bot\\main"
    f_kbot = f_path + ".kbot"
    f_dbot = f_path + ".dbot"

    db = path.isfile(f_dbot)
    kb = path.isfile(f_kbot)

    # if main.dbot exists
    if db and not kb:
        return f_dbot
    # if main.kbot exists
    elif kb and not db:
        return f_kbot
    # if both exist
    elif kb and db:
        # [TODO] Make error better
        raise Exception("Both main.kbot and main.dbot exist")
    # if neither exist
    else:
        # [TODO] Make error better
        raise Exception("No main file exists")
        

def main():
    f_path = resolveMain()
    print(f_path)

main()