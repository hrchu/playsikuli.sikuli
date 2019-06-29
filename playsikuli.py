switchApp("LINE.app")
wait("1561637960646.png", 10)
click("1561637635140.png")
wait(Pattern("1561644160674.png").similar(0.91), 3)
type("let's simulate error occurred!\n")
sleep(1)
try: 
    wait(Pattern("1561640069895.png").similar(0.81), 10)
    #popup('Success!')
finally:
    closeApp("LINE.app")
