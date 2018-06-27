"""

goal is to classify message types in a dialog and use this to model a sequence of transactions in a conversation

this model should be able to predict the next dialog act

FOR INSTANCE:

<start of conversation>
hello! == greeting
how are you today? == personal question
I'm quite well, busy. how about yourself? == answer and response
Actually I'm quite tired, I think I'm going home == disengaging statement
oh, I'm sorry to hear that, have a good evening == empathy and valediction/farewall
<end of conversation>


DIALOG ACTS
greeting/initiation
question/inquiry/request
answer/response
statement/opinion/belief
command/imperative/instruction
farewell/valediction/disengage

"""