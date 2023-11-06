from pystyle import *
import pyshorteners as short


print(Box.Lines(' [+] this app for making shortcut for URL [+]'))


url = Write.Input('please inter URL that you want to make it short :' ,Colors.light_red ,interval=0.1 )

url_short = short.Shortener()

Write.Print(url_short.tinyurl.short(url),Colors.light_red ,interval=0.1)

input('\npress any Key to Exit....')