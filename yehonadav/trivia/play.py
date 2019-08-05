from game import Category, Difficulty, Trivia


class Question:
    import random

    def __init__(self, question: dict):
        self.data = question
        self.correct_answer = question['correct_answer']
        self.answers = [*question['incorrect_answers'], question['correct_answer']]
        Question.random.shuffle(self.answers)
        for i, answer in enumerate(self.answers):
            if answer == self.correct_answer:
                self.correct_index = i
                break

    def ask(self):
        print(self.data['question'])
        for i, answer in enumerate(self.answers):
            print(f'  ({i+1}) {answer}')
        i = int(input("select an answer:")) - 1
        if self.answers[i] == self.correct_answer:
            return True


class Score:
    value = 0
    correct = 0
    wrong = 0

    @staticmethod
    def inc(difficulty: Difficulty):
        if difficulty.name == difficulty.Easy.name:
            Score.value += 10
        elif difficulty.name == difficulty.Medium.name:
            Score.value += 30
        elif difficulty.name == difficulty.Hard.name:
            Score.value += 100
        else:
            raise Exception(f"unknown difficulty level {difficulty.name}")


start_menu = """
			     . ...
			 .''.' .    '.
		    . '' ".'.:I:.'..  '.
		  .'.:.:..,,:II:'.'.'.. '.
		.':.'.:.:I:.:II:'.'.'.'.. '.
	      .'.'.'.'::.:.:.:I:'.'.'.'. .  '
	     ..'.'.'.:.:I::.:II:.'..'.'..    .
	    ..'.'':.:.::.:.::II::.'.'.'.'..   .
	   ..'.'.'.:.::. .:::II:..'.'.'.'.'.   .
	  .':.''.':'.'.'.:.:I:'.'.'.'.'.. '..  ..
	  ':. '.':'. ..:.::.::.:.'..'  ':.'.'.. ..
	 .:.:.':'.   '.:':I:.:.. .'.'.  ': .'.. . ..
	 '..:.:'.   .:.II:.:..   . .:.'. '.. '. .  ..
	.. :.:.'.  .:.:I:.:. .  . ..:..:. :..':. .  '.
       .:. :.:.   .:.:I:.:. .    . ..:I::. :: ::  .. ..
       .. :'.'.:. .:.:I:'.        ..:.:I:. :: ::.   . '.
       '..:. .:.. .:II:'         ,,;IIIH.  ::. ':.      .
      .:.::'.:::..:.AII;,      .::",,  :I .::. ':.       .
      :..:'.:II:.:I:  ,,;'   ' .;:FBT"X:: ..:.. ':.    . .
     .. :':III:. :.:A"PBF;.  . .P,IP;;":: :I:..'::. .    ..
     . .:.:II: A.'.';,PP:" .  . ..'..' .: :.::. ':...  . ..
     . .: .:IIIH:.   ' '.' .  ... .    .:. :.:.. :...    .'
     . .I.::I:IIA.        ..   ...    ..::.'.'.'.: ..  . .
      .:II.'.':IA:.      ..    ..:.  . .:.: .''.'  ..  . .
     ..::I:,'.'::A:.  . .:'-, .-.:..  .:.::AA.. ..:.' .. .
      ':II:I:.  ':A:. ..:'   ''.. . : ..:::AHI: ..:..'.'.
     .':III.::.   'II:.:.,,;;;:::::". .:::AHV:: .::'' ..
     ..":IIHI::. .  "I:..":;,,,,;;". . .:AII:: :.:'  . .
     . . IIHHI:..'.'.'V::. ":;;;"   ...:AIIV:'.:.'  .. .
      . . :IIHI:. .:.:.V:.   ' ' . ...:HI:' .:: :. .  ..
      . .  ':IHII:: ::.IA..      .. .A .,,:::' .:.    .
      :.  ...'I:I:.: .,AHHA, . .'..AHIV::' . .  :     ..
      :. '.::::II:.I:.HIHHIHHHHHIHHIHV:'..:. .I.':. ..  '.
   . . .. '':::I:'.::IHHHHHHHHMHMHIHI. '.'.:IHI..  '  '  '.
    ':... .  ''" .::'.HMHI:HHHHMHHIHI. :IIHHII:. . . .    .
     :.:.. . ..::.' .IV".:I:IIIHIHHIH. .:IHI::'.': '..  .  .
   . .:.:: .. ::'.'.'..':.::I:I:IHHHIA.'.II.:...:' .' ... . '..
  '..::::' ...::'.IIHII:: .:.:..:..:III:.'::' .'    .    ..  . .
  '::.:' .''     .. :IIHI:.:.. ..: . .:I:"' ...:.:.  ..    .. ..
     .:..::I:.  . . . .IHII:.:'   .. ..".::.:II:.:. .  ...   . ..
  .. . .::.:.,,...-::II:.:'    . ...... . .. .:II:.::  ...  .. ..
   ..:.::.I .    . . .. .:. .... ...:.. . . ..:.::.   :..   . ..
    .'.::I:.      . .. ..:.... . ..... .. . ..::. .. .I:. ..' .
  .'':.: I.       . .. ..:.. .  . .. ..... .:. .:.. .:I.'.''..
  . .:::I:.       . . .. .:. .    .. ..  . ... .:.'.'I'  .  ...
  . ::.:I:..     . . . ....:. . .   .... ..   .:...:.:.:. ''.''
  '.'::'I:.       . .. ....:. .     .. . ..  ..'  .'.:..:..    '
	:. .     . .. .. .:.... .  .  .... ...   .  .:.:.:..    '.
	:.      .  . . .. .:.... . . ........       .:.:.::. .    .
	:. .     . . . . .. .::..:  . ..:.. .        ::.:.:.. .    .
	:.. .    . . .  . .. ..:.:  .. .. .:. ..     ':::.::.:. .   .
	':.. .  . . . .. .. ...::' .. ..  . .:. .     V:I:::::.. .   :.
	 ::. .  . .. .. ... .:.::  .. .  . .. .. .     VI:I:::::..   ''B
	  :.. .   . .. ..:.. ..I:... . .  . .. ... .    VII:I:I:::. .'::
	  ':.. . . . .. ..:..:.:I:.:. .  . .. . .:. .    VHIII:I::.:..':
	   ::..   . . .. ..:..:.HI:. .      . . .... .   :HHIHIII:I::..:
	   ':. .  . .. .. ..:.:.:HI:.    . . .. ..... .   HHHHIHII:I::.'
	    :.. .  . . .. .:.:.:.HI:.      . . .. ... .   IHHHHIHHIHI:'
	     :..  .  . . .. ..:..IH:.     . . .. .. ,,, . 'HHHHHHHHI:'
	     ':..   . . .. ..:.:.:HI..   .  . .. . :::::.  MIH:''""
	      :. . .  . .. ..::.:.VI:.     . . .. .:::'::. HIH
	       :..  .  . .. .:.:.:.V:.    . . . ...::I"A:. HHV
		:. .  .  . .. ..:.:.V:.     . . ....::I::'.HV:
		 :. .  . . . .. .:..II:.  . . . ....':::' AV.'
		  :.. . . .. ... .:..VI:. . . .. .:. ..:.AV'.
		  ':.. . .  .. ..:.:.:HAI:.:...:.:.:.:.AII:.
		   I:. .  .. ... .:.:.VHHII:..:.:..:A:'.:..
		   IA..  . . .. ..:.:.:VHHHHIHIHHIHI:'.::.
		   'HA:.  . . .. ..:.:.:HHHIHIHHHIHI:..:.
		    HIA: .  . . .. ...:.VHHHIHIIHI::.:...
		    HIHI:. .  .. ... .::.HHHIIHIIHI:::..
		    HII:.:.  .  .. ... .::VHHIHI:I::.:..
		    AI:..:..  .  . .. ..:.VHIII:I::.:. .
		   AI:. ..:..  .  . .. ..' VHIII:I;... .
		  AI:. .  .:.. .  .  . ...  VHIII::... .
		.A:. .      :.. .  . .. .:.. VHII::..  .
	       A:. . .       ::. .. .. . .:.. "VHI::.. .
	     .:.. .  .        :.. .:..... .::.. VHI:..
	    ... . .  .     . . :.:. ..:. . .::.. VI:..  .
	   .. .. .  .    . . ...:... . .. . .:::. V:..  .
	  '.. ..  .   .  .. ..:::.... .:. . ..::.. V..  .
	. . .. . .   . . .. ..:::A. ..:. . . .::.. :..
       . .. .. .. . .  . ... ..::IA.. .. . .  ..::. :..  .
      .. .. ... . .  .. .... .:.::IA. . .. . ..:.::. :.  .
     . . . .. .   . . .. ..:..:.::IIA. . .  .. .:.::. :. .
    .. . .  .   . . .. ... ..:.::I:IHA. .  . . ..:.::. . .
   .: ..  .  .   . . ... .:.. .:I:IIHHA. .  . .. .::I:. .
  .::.  .     . . .. ..:. .::.:IIHIIHHHA.  .  .. ..:I:. . .
  A::..      .  .  ...:..:.::I:IHIHIHHHHA.  .  . ..::I:. .
 :HI:.. .       . .. .:.:.::I:IHIHIIHIHHHA. .   .. .::I:. ..
 AI:.. .. .    . .. .:.:.::II:IHIIIHIHIHHHA.  .  . ..::I:. ..
:HI:.. . .   .  . .. .::.:I:IHIHIIIHIHIIHHHA..  . .. .::I:. ..
AI:.:.. .  .  .  ... .::.::I:IHIIHIHIHIHIHIHHA. .  . ..::I:. .
HI:. .. . .  .  . .. .:..::IIHIHIHIIIIWHIIHHMWA.  . . .:::I:. . .
HI:.. . .  .   . .. ..:.::I:IIHHIIHIHIHIHHMMW"  '.. . ..:::II: . .
HI::.. .  .   .  .. .:..:::IIHIHIIWIWIIWMWW" .    .. . ..::III: .  .
HI::... . . .  . ... ..:.:::IIHIWIWIWMWMWW. .  .   . .. .:.:III. .   .
II::.:.. . .  .  .. ......:..IHWHIWWMWMW".. . . . . '... .:.:IHI:..    .
II:I::.. .  .   .  . .....::.:IHWMWWWMW:.. .  .  . .  .:..:::IIHII..
:II:.:.:.. .  .   . ......:.:.:IWWMWWW:.:.. .  .  .  . :...:.:IHHI:..
 HI::.:. . . .  .  . ...:.::.::.VWMWW::.:.:.. .  . .. . :.. ..:IHHI::.'-
 HII::.:.. .  .  . .. .:..:.'.  'WWWI::.::.:.. . .  . .. ':...:II:IIII::
 III::.:... .  .  . ...:.:... .   WII:I::.:.. .  .  .. . . :.:::...::.::
  VII::.:.. . . . .. ...:....      VHI:I::.:.. .  . ... .. .::.:..:.:..:
   VII::.:.. . .  . ..:.::.. .     :HHII:I::.:.. . . .. ..  .'::':......
   III:I::.. .. . . .. .:.:.. .    :VHIHI:I::.:... . . .. .. .':. .. .AH
  AA:II:I::.. . . .  .. ..:.. . .  ::HHIHII:I::.:... .. .. ... .:.::AHHH
 AHH:I:I::.:.. .  . .. ..:.:.. .   ::VHHHVHI:I::.:.:.. ..:. .::.A:.AHHHM
 HHHAII:I::.:.. . . . .. ..:.. . . :::HIHIHIHII:I::.:.. .. .:. ..AHHMMM:
AHHHH:II:I::.:.. . . .. ..:.:.. . .:I:MMIHHHIHII:I:::.:. ..:.:.AHHHMMM:M
HHHHHA:II:I::.. .. . . .. .:... . .:IIVMMMHIHHHIHII:I::. . .. AHHMMMM:MH
HHHHHHA:I:I:::.. . . . ... ..:.. ..:IHIVMMHHHHIHHHIHI:I::. . AHMMMMM:HHH
HHHHHMM:I::.:.. . . . .. ...:.:...:IIHHIMMHHHII:.:IHII::.  AHMMMMMM:HHHH
HHHHHMMA:I:.:.:.. . . . .. ..:.:..:IIHHIMMMHHII:...:::.:.AHMMMMMMM:HHHHH
HHHHHMMMA:I::... . . . . .. ..:.::.:IHHHIMMMHI:.:.. .::AHMMMMMMM:HHHHHHH
VHHHHMMMMA:I::.. . .  . . .. .:.::I:IHHHIMMMMHI:.. . AHMMMMMMMM:HHHHHHHH
 HHHMMMMMM:I:.:.. . .  . . ...:.:IIHIHHHIMMMMMHI:.AHMMMMMMMMM:HHHHHHHHHH
 HHHHMMMMMA:I:.:.. .  .  . .. .:IIHIHHHHIMMMMMH:AMMMMMMMMMMM:HHHHHHHHHHH
 VHHHMMMMMMA:I:::.:. . . . .. .:IHIHHHHHIMMMV"AMMMMMMMMMMMM:HHHHHHHHHHHH
  HHHHHMMMMMA:I::.. .. .  . ...:.:IHHHHHHIM"AMMMMMMMMMMMM:HHHHHHHHHHHHHH
  VHHHHHMMMMMA:I:.:.. . . .  .. .:IHIHHHHI:AMMMMMMMMMMMIHHHHHHHHHHHHHHHH
   VHHHHHMMMMMA:I::.:. . .  .. .:.:IHHHV:MMMMMIMMMMMMMMMMMMMHHHHHHHHV::.
    VHHHHMMMMMMA:::.:..:.. . .. .:::AMMMMMMMM:IIIIIHHHHHHHHHHHHHHHV:::..
     HHHHHMMMIIIA:I::.:.:..:... AMMMMMMMMMM:IIIIIIHHHHHHHHHHHHHHHV::::::
     VHHHHMMIIIIMA:I::::.::..AMMMMMMMMMMM:IIIIIIIHHHHHHHHHHHHHHV::::::::
      HHHHMIIIIMMMA:II:I::AIIIMMMMMMMMMM:IIIIIIIHHHHHHHHHHHHHHV:::::::::
      VHHHHIIIMMMMMMA:I:AIIIIIIMMMMMM:IIIIIIIIHHHHHHHHHHHHHHV::::::::"'
       HHHHHIIMMMMMMIMAAIIIIIIIIMMM:IIIIIIIIHHHHHHHHHHHHHHHV:::::""'
       VHHHIIIIMMMMIIIIIIIIIIIIII:IIIIIIIIHHHHHHHHHHHHHHHV::""'
	VHHIIIMMMMMIIIIIIIIIIIIIIIIIIIIIHHHHHHHHHHHHHHHV
	 VHHIMMMMMMMIIIIIIIIIIIIIIIIIHHHHHHHHHHHHHV
	  VHHHMMMMMMMMIIIIIIIIIIIHHHHHHHHHHHV
	   VHHHMMMMMMMMMMMMMHHHHHHHHV
==========================================================================
                         Ready for Trivia ?
==========================================================================                         	   
"""
print(start_menu)
username = input("your name:")


while True:
    try:
        questions = int(input("enter number of questions:"))
        category = Category(int(input('choose category:\n   ' + '\n   '.join((f"({i.value}) {i.name}" for i in Category)) + '\n')))
        difficulty = Difficulty(input('choose difficulty:\n   ' + '\n   '.join((f"({i.value}) {i.name}" for i in Difficulty)) + '\n'))

        print("loading questions...")
        opentdb = Trivia()
        questions = [Question(question) for question in opentdb.request(questions, category, difficulty)['results']]
        print("we are set to go!")

        for question in questions:
            answer = question.ask()
            if answer is True:
                print('correct!')
                Score.inc(difficulty)
                Score.correct += 1
            else:
                print(f'wrong! the correct answer is ({question.correct_index+1})')
                Score.wrong += 1
            print('')

        again = input("would you like to try more questions(y/n)?")
        if again == 'n':
            break
    except:
        import traceback
        print(traceback.format_exc())
        print('rebooting... \n\n\n')
        Score.value = 0
        Score.wrong = 0
        Score.correct = 0


final_menu = """
===========================================
                  SCORE                
===========================================

        name: {}
        points: {}
        correct answers: {}
        wrong answers: {}
""".format(username, Score.value, Score.correct, Score.wrong)
print(final_menu)
