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

# colorama.init(): Ініціалізує палітру кольорів для поточної платформи.
# colorama.deinit(): Завершує роботу з палітрою кольорів.
# colorama.Fore та інші атрибути кольорів: Надає зручний доступ до ANSI-колірів для тексту та фону.
# colorama.Back: Аналогічно, але для кольору фону.
# colorama.Style: Надає доступ до стилів тексту, таких як жирний, курсив, підкреслення і т.д.
