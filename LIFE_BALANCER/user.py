from no_such_goal_error import NoSuchGoalError

class User(object):

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.points = 0
        self.goals = []
        self.history = []

    def addGoal(self, goal):
        self.goals.append(goal)

    def removeGoal(self, goal):
        try:
            self.goals.remove(goal)
        except ValueError as error:
            raise NoSuchGoalError
