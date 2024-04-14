def get_data(url, filename):
    import requests
    import pathlib
    ## make the data folder
    path = pathlib.Path('data')
    path.mkdir(exist_ok=True)

    
    request = requests.get(url)
    with open(f"./data/{filename}", 'wb') as fb:
        fb.write(request.content)
    pass

def checkFile(path:str):
    import pathlib, os
    path = pathlib.Path(path)
    return not os.path.exists(path)
