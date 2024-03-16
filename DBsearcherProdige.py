import os
from pystyle import Colorate, Colors
#crée par ProdigeDuNet
os.system('cls')
#crée par ProdigeDuNet
def search_files(search_term, database_folder, max_results=10):
    results = []
    results_found = 0
    for root, _, files in os.walk(database_folder):
        if results_found >= max_results:
            break
        for file in files:
            if file.endswith(('.txt', '.csv', '.sql')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if results_found >= max_results:
                            break
                        if search_term in line:
                            result_str = f'{line.strip()}'
                            results.append(result_str)
                            results_found += 1
    return results

def main():
    database_folder = r"C:\dest1\DataBase"

#crée par ProdigeDuNet

    
    print(Colorate.Horizontal(Colors.red_to_white,"░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗███████╗██████╗░        "))
    print(Colorate.Horizontal(Colors.red_to_white,"██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗       "))
    print(Colorate.Horizontal(Colors.red_to_white,"╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║█████╗░░██████╔╝        by Prodige ")) 
    print(Colorate.Horizontal(Colors.red_to_white,"░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║██╔══╝░░██╔══██╗        "))
    print(Colorate.Horizontal(Colors.red_to_white,"██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║███████╗██║░░██║"))
    print(Colorate.Horizontal(Colors.red_to_white,"╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝"))
    print(Colorate.Horizontal(Colors.red_to_white,"PPPPPPPP    RRRRRRRR   OOOOOOOO   DDDDDDDD    IIIIIIII   GGGGGGGG   EEEEEEEE",))
    print(Colorate.Horizontal(Colors.red_to_white,"PP    PPP  RR    RRR  OO      OO  DD    DDD     III    GG    GGG    EE",))
    print(Colorate.Horizontal(Colors.red_to_white,"PPPPPPPP   RRRRRRRR   OO      OO  DD    DDD     III    GG           EEEEE ",))
    print(Colorate.Horizontal(Colors.red_to_white,"PP         RR  RR     OO      OO  DD    DDD     III    GG   GGGG    EE",))
    print(Colorate.Horizontal(Colors.red_to_white,"PP         RR    RR    OOOOOOOO   DDDDDDDD    IIIIIIII   GGGGGG     EEEEEEEE",))
    term = input(Colorate.Horizontal(Colors.red_to_white, "Entre ce que tu veux chercher dans tes db de pd ou appuye sur q pour quitter => "))
 #crée par ProdigeDuNet
    print("recherche en cours")
    while term.lower() != 'q':
        results = search_files(term, database_folder)

        if results:
            print(Colorate.Horizontal(Colors.white_to_red, "Résultats Trouver :"))
            for result in results:
                print(result)

        else:
            print(Colorate.Horizontal(Colors.white_to_red, "Aucun Résultats n'as étais trouver"))

        term = input(Colorate.Horizontal(Colors.red_to_white, "Entre ce que tu veux chercher dans tes db de pd ou appuye sur q pour quitter => "))    

if __name__ == "__main__":
    main()


#crée par ProdigeDuNet
#crée par ProdigeDuNet
#crée par ProdigeDuNet
#crée par ProdigeDuNet
#crée par ProdigeDuNet

#crée par ProdigeDuNet
#crée par ProdigeDuNet