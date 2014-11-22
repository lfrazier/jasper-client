# -*- coding: utf-8-*-
import re
import wordstonumbers
import testing

WORDS = ["SET", "MINUTE", "TIMER"]


def isValid(text):
    """
        Returns True if the input is related to setting a timer.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    regex = r'\bset\s+((a|an)\s+)?(\w*\s*minute\s+)?timer'
    return bool(re.search(regex, text, re.IGNORECASE))


def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, by setting a
        timer. Gives a FINAL COUNTDOWN during the final 5 seconds.

        Notifies the user when the timer is 50 percent
        finished, 75 percent finished, 90 percent finished, etc. Also
        notifies when there is 1 minute left and doesn't give any more
        notifications until the Final Countdown!

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    timeString = ""
    # If the text contains the word "minute", look at the preceding
    # word to get the number. Otherwise, ask the user for a number.
    if "minute" in text:
      words = text.split()
      words.reverse()
      try:
        timeString = words[words.index("minute") + 1]
      except ValueError:
        mic.say("Are you French, Clyde?")
    else:
      mic.say("How long?")
      timeString = mic.activeListen().split()[0]
    timeValue = convertStringToNumber(timeString)
    print str(timeValue)


def convertStringToNumber(string):
  number = 0
  if string.isdigit():
    number = int(string)
  elif string == "a":
    number = 1
  else:
    number = wordstonumbers.WordsToNumbers().parse(string)
  return number

#Testing
def testIsValid(text):
  print text + ": " + str(isValid(text))


def testHandle(text):
  mic = testing.FakeMic()
  print "\"" + text + "\""
  handle(text, mic, "")
  print


if __name__ == "__main__":
    print "Test isValid():"
    testIsValid("test")
    testIsValid("Set a timer")
    testIsValid("Set a 5 minute timer")
    testIsValid("Set the table")
    testIsValid("Set an 8 minute timer")
    testIsValid("Set a minute timer")
    testIsValid("Set a  5 minute  timer")
    testIsValid("Set a five minute timer")
    testIsValid("Set an timer")
    testIsValid("Set timer")
    print
    print "Test handle():"
    testHandle("Set a 5 minute timer")
    testHandle("Set an 8 minute timer")
    testHandle("Set a minute timer")
    testHandle("Set a  5 minute  timer")
    testHandle("Set a five minute timer")
    testHandle("Set an timer")
    testHandle("Set timer")
    testHandle("Set a timer")
