# from turtle import Turtle, Screen, color
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color('red', 'blue')
# timmy.forward(250)
# timmy.left(90)
# timmy.forward(250)
# timmy.left(90)
# timmy.forward(250)
# timmy.left(90)
# timmy.forward(250)
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)





