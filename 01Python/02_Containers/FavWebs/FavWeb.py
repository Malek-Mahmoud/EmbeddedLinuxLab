import webbrowser
def FireFox(link):
    Browser = webbrowser.get('firefox')
    Browser.open(link)
    

myFavWebs = {
    "Facebook":"https://www.facebook.com/",
    "Youtube":"https://www.youtube.com/",
    "C++Insigts":"https://cppinsights.io/"
}