import colorama
import inspect
colorama.init()

print(f"{colorama.Fore.RED}Червоний текст{colorama.Style.RESET_ALL}")
#Додала кольоровий текст

print(f"{colorama.Back.GREEN}Зелений фон{colorama.Style.RESET_ALL}")
#Зробила колір фону колір фону

print(f"{colorama.Style.BRIGHT}Яскравий текст{colorama.Style.RESET_ALL}")
#Використала стиль тексту

colorama.deinit()
