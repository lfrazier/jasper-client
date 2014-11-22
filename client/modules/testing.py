""" Testing code for writing modules """

class FakeMic:
  """
      A fake microphone that subs command line input/output for
      microphone and speaker I/O.
  """
  def say(self, message):
    """
    Just prints the message to the console. With a real Mic object, the text
    would be spoken aloud.
    """
    print "say: " + message


  def activeListen(self):
    """
    "Listens" for text on the command line. With a real Mic object, the user
    would say the text aloud.
    """
    return raw_input("listening... ")
