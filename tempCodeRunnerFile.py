 elif 'play song'in data1:
                address="C:\\Users\\91860\\Songs"
                listsong = os.listdir(address)
                print(listsong)
                os.startfile(os.path.join(address,listsong[0]))
                songprompt="playing Skyfall by Adele"
                speechtx(songprompt)