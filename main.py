import turtle
import pandas

screen = turtle.Screen()
image = "India.gif"
screen.title("Indian States Game")
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("india_states.csv")
guessed_states = []

while len(guessed_states)<31:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's another state name?").title()
    all_states = data["state"].to_list()

    if answer_state == "Exit":
        remaining = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(remaining)
        df.to_csv('states_to_learn.csv')
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

