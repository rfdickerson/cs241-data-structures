from flask import Flask, render_template, request
from eightpuzzle import EightPuzzleSolver
app = Flask(__name__)

def parseinput(stringinput):
    l = stringinput.split(",")
    output = []
    for element in l:
        if data is 'None':
            output.append(None)
        else
            output.append(int(element))
    return output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    print 'solving puzzle...'
    initial = request.form['initial']
    goal = request.form['goal']
    solver = EightPuzzleSolver(initial, goal)
    solution = solver.solve()
    return render_template('solution.html',
            solution=solution
            )


if __name__ == "__main__":

    app.run(debug=True)
