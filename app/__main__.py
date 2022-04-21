
def main():
    i = input('[C]lient app\n[S]erver app\n:')
    if i in ['c', 'C']:
        os.system('python3 app/client_App.py')
    elif i in ['s', 'S']:
        os.system('python3 app/server_App.py')


if __name__ == '__main__':
    import os
    main()
    