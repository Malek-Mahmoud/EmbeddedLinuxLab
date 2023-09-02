import FavWeb

print("Choose the a Website: ")
for web in FavWeb.myFavWebs.keys():
    print(web)

selectedWeb = input()
if selectedWeb in FavWeb.myFavWebs.keys():
    FavWeb.FireFox(FavWeb.myFavWebs.get(selectedWeb))

else:
    print("Invald input")