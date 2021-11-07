import pywhatkit as kit
import webbrowser as wb

name = ("Artist: \n 1)Justin Biber \n 2)TRAVIS \n 3)DOJA CAT \n 4)Ariana Grande \n 5)XXXTENTACION \n 6)Don toliver \n 7)Spotify Playlist")

print(name)

number = input("Enter the number: ")

if number == "1":
    print(" Song Names: \n 1)Sorry \n 2)What Do You Mean \n 3)Peaches \n 4)Intentions \n 5)Stay \n 6)Let Me Love You")
    song_number = input("Enter the number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=BerNfXSuvJ0")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=I7rySXI7DDc")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=BydBU2pCkU8")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=yrYxt1FZYgA")
    elif song_number == "5":
        kit.playonyt("https://www.youtube.com/watch?v=yWHrYNP6j4k")
    elif song_number == "6":
        kit.playonyt("https://www.youtube.com/watch?v=SMs0GnYze34")
    else:
        print("INVALID")

elif number == "2":
    print(" Song Names: \n 1)Sicko Mode \n 2)Goosebumps \n 3)Highest In The Room \n 4)Out West \n 5)stargazing \n 6)Durag Activity \n 7)5% Tint")
    song_number = input("Enter the number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=f2YWfeFRZO0")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=Mqr70DmMgYw")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=pAcfgzpN-TU")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=uKvE2Yve9vc")
    elif song_number == "5":
        kit.playonyt("https://www.youtube.com/watch?v=f8KfdkBKI0k")
    elif song_number == "6":
        kit.playonyt("https://www.youtube.com/watch?v=LklUW6efb-s")
    elif song_number == "7":
        kit.playonyt("https://www.youtube.com/watch?v=yKGRLxdDTh4")
    else:
        print("INVALID")

elif number == "3":
    print(" Song Names: \n 1)Need to know \n 2)Women \n 3)Get Into it \n 4)Kiss Me More")
    song_number = input("Enter the number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=2fEAyHNekF4")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=L_5igjD_fKU")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=IsiHvXlXbkc")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=1oMgxa32A7g")
    else:
        print("INVALID")

elif number == "4":
    print("Song names: \n 1)Motive \n 2)Boyfriend \n 3)34+35 \n 4)positions")
    song_number = input("Enter the number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=J-Jy9PogRwI")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=reCSdoGbEAk")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=qexlDD70mio")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=swYMG7X1iDQ")
    else:
        print("INVALID")

elif number == "5":
    print(" Song Names: \n 1)Hope \n 2)Jocelyn Flores \n 3)Up Up And Away \n 4)EveryBody Dies In Their Nightmares \n 5)The Remedy For A Broken Heart")
    song_number = input("Enter the number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=58xKTGxmeHI")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=7XhwUbf_O9g")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=_NTkMNFS-Cw")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=HdYmhf7cclI")
    elif song_number == "5":
        kit.playonyt("https://www.youtube.com/watch?v=C-ThptbFogs")
    else:
        print("INVALID")
elif number == "6":
    print("Song Names: \n 1)Lemonade \n 2)No Idea \n 3)Flocky Flocky \n 4)After Party \n 5)Mystery Lady")
    song_number = input("Enter The Number: ")
    if song_number == "1":
        kit.playonyt("https://www.youtube.com/watch?v=U-fcXjcJXks")
    elif song_number == "2":
        kit.playonyt("https://www.youtube.com/watch?v=2QajgEpKqCA")
    elif song_number == "3":
        kit.playonyt("https://www.youtube.com/watch?v=uzC1_Mrf2fA")
    elif song_number == "4":
        kit.playonyt("https://www.youtube.com/watch?v=v8Q4BSgBkRc")
    elif song_number == "5":
        kit.playonyt("https://www.youtube.com/watch?v=S2Bqm02qxXE")
    else:
        print("INVALID")
elif number == "7":
    wb.open("https://open.spotify.com/playlist/1C9hralKpJXlVX5i0qkYjd?si=097650dc0ddc4f21")

else:
    print("Please Re-enter the number")