#imports the library

from dragonfly import (BringApp, StartApp, Function, Mimic, Grammar, AppContext, MappingRule, Integer, Key, Text, Dictation, Choice, Pause, Mouse)

def start_day():
    # Mimic('open', 'dryfly')
    # Pause('500')
    Mimic('open', 'pie')
    Mimic('connect', 'pre')

class GlobalMappings(MappingRule):
    mapping = {  
		'find [<text>]': Key("c-f") + Pause("10") + Text("%(text)s"),
        'back space': Key('backspace'),
        'nip': Key('escape'),
        'snap': Key('a-tab'),
        'snap hold': Key('alt:down, tab'),
        'pick': Key('enter,alt:up'),
        'slap': Key('c-tab'),
        'down': Key('down'),
        'down <number>': Key('down:%(number)d'),
        'up': Key('up'),
        'up <number>': Key('up:%(number)d'),
        'ut': Key("pgup"),
        'dut': Key("pgdown"),
        'left [<number>]': Key('left:%(number)d'),
        'left <number> word': Key("ctrl:down, left:%(number)d, ctrl:up"),
        'right [<number>]': Key('right:%(number)d'),
        'right <number> word': Key("ctrl:down, right:%(number)d, ctrl:up"),
        "camel [under] <camel_text>": Text("%(under)s%(camel_text)s"),
        "snake [<under>] <snaketext>": Text("%(under)s%(snaketext)s"),
        "dash [<dash>] <dashtext>": Text("%(dash)s%(dashtext)s"),
        "paschal [<pascaltext>]": Text("%(pascaltext)s"),
        "title [<titletext>]": Text("%(titletext)s"),
        'select down <number>': Key("home, shift:down, down:%(number)d, up, end, shift:up"),
        'select up <number>': Key("end, shift:down, up:%(number)d, down, home, shift:up"),
        'select right <number>': Key("ctrl:down, shift:down, right:%(number)d, ctrl:up, shift:up"),
        'select left <number>': Key("ctrl:down, shift:down, left:%(number)d, ctrl:up, shift:up"),
        'line end [<number>]': Key("end") + Key("left:%(number)d"),
        'line home [<number>]': Key("home") + Key("right:%(number)d"),
        'undo [<number>]': Key("c-z:%(number)d"),
        'redo [<number>]': Key("c-y:%(number)d"),
        'snap load': Key('w-4') + Pause("10") + Key('c-1') + Pause("10") + Key('f5') + Pause("10") + Key('a-tab'),
        
        'to files': Key("w-1"),
        'to Outlook': Key("w-2"),
        'to Teams': Key("w-3"),
        'to Web': Key("w-4"),
        'to pie': Key("w-5") + Pause('50') + Key("enter"),
        'to code': Key("win:down, 5, 5, win:up") + Pause('50') + Key("enter"),
        'to stud': Key("w-6"),
        'to postman': Key("w-7"),
        'to notepad': Key("w-8"),
        'to dragon': Key("w-9"),
        
        'craig pass': Text("conec#20"),
        'Prod pass': Text("1qaz@WSX3edc$RFV"),
        'Sand pass': Text("1qaz@WSX3edc"),

        # 'open dryfly': StartApp(R"C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE\devenv.exe") + Pause('500') + Key("cs-o,a-d") + Text('D:\GitProjects\dryfly\FreeStone\DryFly.sln') + Key('enter'),
        # 'open MC API': StartApp(R"C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\Common7\IDE\devenv.exe") + Pause('500') + Key("cs-o,a-d") + Text('D:\GitProjects\marketing-content-api\src\MarketingContent.Api.sln') + Key('enter'),
        'open pie': StartApp(R"C:\Users\csalzsieder\AppData\Local\Programs\Microsoft VS Code\Code.exe") + Pause('500') + Key("cs-o,a-d") + Key("c-k,c-o,a-d") + Pause('50') + Text('C:\NatLink\NatLink\MacroSystem') + Key("enter:2"),
        'open react': StartApp(R"C:\Users\csalzsieder\AppData\Local\Programs\Microsoft VS Code\Code.exe") + Pause('500') + Key("cs-o,a-d") + Key("c-k,c-o,a-d") + Pause('50') + Text('D:\GitProjects\react-components\src') + Key("enter:2"),
        'connect pre': StartApp("C:\Program Files (x86)\Pritunl\pritunl.exe") + Pause("300") + Mouse("[0.57, 0.29], left") + Pause('50') + Mouse("[0.57, 0.29], left") + Pause('400') + Text("1qaz@WSX3edc$RFV") + Pause('50') + Mouse("[0.55, 0.29], left"),
        '[<number>] tab': Key('tab:%(number)d'),
        'Start day': Function(start_day),

        # Temporary
        'flag it': Key("enter") + Text("//ToDo: DF-10303 remove unused fields, delete later") + Key("down,c-k,c-c"),
        }

    extras=[
        Integer('tab', 1, 10),
        Integer('number', 1, 9999),
        Dictation("camel_text", default="").camel(),
        # Define a Dictation element that produces snake case text,
        # e.g. hello_world.
        Dictation("snaketext", default="").lower().replace(" ", "_"),
        Dictation("dashtext", default="").lower().replace(" ", "-"),
        # Define a Dictation element that produces text matching Python's
        # class casing, e.g. DictationContainer.
        Dictation("pascaltext", default="").title().replace(" ", ""),
        Dictation("titletext", default="").title().replace(" ", " "),
        # Allow adding underscores before cased text.
        Choice("under", {"under": "_"}, default=""),
        Choice("dash", {"dash": "-"}, default=""),
        Dictation("text")
    ]

grammar=Grammar('Global')
grammar.add_rule(GlobalMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None

