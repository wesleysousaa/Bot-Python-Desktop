import pyautogui

pyautogui.PAUSE = 1

pyautogui.press("win")

pyautogui.write("Bloco de Notas")

pyautogui.press("backspace")

pyautogui.press("enter")

pyautogui.write("Bot muito simples feito em python. by WesleySousaa")

with pyautogui.hold("ctrl"):
    pyautogui.press("s")

pyautogui.write("mensagem para voce")

pyautogui.press("enter")