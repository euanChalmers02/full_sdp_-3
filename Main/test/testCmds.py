import time
import unittest

from Main.fnd.SoundCode.Buttons.Singleton import get_instate_of_state

state = get_instate_of_state()


class scan_scenarios(unittest.TestCase):

    def test_assert_commands_create(self):
        pass

    def test_assert_command_change_as_expected(self):
        state.commandInterface("AA")
        self.assertEqual(state.get_state(), "pause")
        state.commandInterface("AA")
        self.assertEqual(state.get_state(), "Scan")
        state.commandInterface("A")
        self.assertEqual(state.get_state(), "dist")
        state.commandInterface("A")
        self.assertEqual(state.get_state(), "Scan+ocr")
        return

    def test_assert_handle_unknown_cmd(self):
        # unknown / unmapped command
        res = state.commandInterface("xyxysyws")
        self.assertFalse(res)

    def test_user_story_one(self):
        pass


if __name__ == '__main__':
    unittest.main()
