# Puzzle Solver

* Due: April 7, 2014
* Deliverables: eightpuzzle.py

# Overview

You are creating a eight puzzle solver for this assignment. This puzzle
consists of 8 puzzle pieces on a 3x3 grid. There is one missing piece, but you
can slide the pieces around to fill that gap. You will be given an initial
state for the puzzle and a goal state, and your solver will test all possible
strategies for solving the puzzle, and return a step by step process for
solving the puzzle.

# Specification

The template for your puzzle is in eightpuzzle.py. There is a BadMoveException
object that can be raised when you tell a PuzzleState to slide in a certain
direction but it is illegal to do so. The PuzzleState class contains the
current state of the game board, the numbers in each tile, and the parent game
state in which this game state was generated from. For the initial game state,
the parent can be set to None. There is a moveUp, down, left, and right method
that will return a new PuzzleState instance with the pieces slid in the correct
position. If it is an illegal move, this method should raise a
BadMoveException. The str function should return a human readable
representation of the 3x3 grid that is two-dimensional, not a one-dimensional
list of integers. The eq function will be overriden to check if the values in
the PuzzleState match the values in another PuzzleState.

The EightPuzzleSolver has a constructor that takes a initial state and a goal
state. When the solve method is invoked, the breadth-first search algorithm
will build a game tree for all possible moves that can be made from that root.
A list of visited PuzzleStates will be tracked in a list so that you do not get
into an infinite loop checking for the same moves. Once a PuzzleState is
generated that matches the goal, then the searching stage is complete. Now,
backtrack to generate the solution. Create a new array for the steps. Start
with the goal PuzzleState, and travel to the parent PuzzleState. Continue until
the parent is None, therefore you have found the initial state. Print the
result.


