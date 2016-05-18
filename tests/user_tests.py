from nose.tools import *
from LIFE_BALANCER.user import User
from LIFE_BALANCER.no_such_goal_error import NoSuchGoalError

class TestUser:

    def setUp(self):
        self.user = User("username", "password", "e-mail")
        self.exampleGoal = "To be the very best like no one ever was"

    def test_shouldStartWithEmptyGoalsAndZeroMoney(self):
        assert_equal(self.user.points, 0)
        assert_equal(self.user.goals, [])

    def test_newUserShouldHaveNoHistory(self):
        assert_equal(self.user.history, [])

    def test_shouldBeAbleToAddGoals(self):
        self.user.addGoal(self.exampleGoal)
        assert_equal(self.user.goals, [self.exampleGoal])

    def test_shouldBeAbleToRemoveGoalsWhenItExists(self):
        self.user.addGoal(self.exampleGoal)
        self.user.removeGoal(self.exampleGoal)
        assert_equal(self.user.goals, [])

    @raises(NoSuchGoalError)
    def test_shouldRaiseNoSuchGoalError(self):
        self.user.removeGoal(self.exampleGoal)
