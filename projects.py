THE_AWAKENING = "The Awakening"
PORTFOLIO = "Portfolio Website"
SPACEBAR_INVADERS = "Spacebar Invaders"
SMACK_CHAT = 'Smack Chat'
MINUTES_TO_MIDNIGHT = "Minutes to Midnight"
FAST_SQRT = "Fast Square Root"
CA_RULES = "Elementary Cellular Automata"

class Project:
    def __init__(self, name, desc, tech_stack, git, other_source=None, source_name = None, git_service_name="GitHub"):
        self.name = name
        self.desc = desc
        self.tech_stack = tech_stack
        self.github = git
        self.service_name = git_service_name
        self.other_source = other_source
        if self.other_source is not None:
            self.has_other_source = True
            self.source_name = source_name
        else:
            self.has_other_source = False

PROJECT_DICT = {
    THE_AWAKENING: Project(THE_AWAKENING, "text based adventure game", ["C++"], "https://github.com/JoJaJones/The-Awakening", "https://repl.it/@JoJaJones/The-Awakening?lite=true", "repl.it"),
    PORTFOLIO: Project(PORTFOLIO, "this website", ["flask", "bootstrap", "CSS", "HTML", "JavaScript"], "https://github.com/JoJaJones/Portfolio-Website"),
    SPACEBAR_INVADERS: Project(SPACEBAR_INVADERS, "webpage and JS game", ["HTML", "CSS", "JavaScript"], "https://github.com/JoJaJones/SpacebarInvaders", "https://jojajones.github.io", "github.io"),
    SMACK_CHAT: Project(SMACK_CHAT, "slack clone", ["Kotlin", "Android Studio", "XML"], "https://bitbucket.org/planetflamingunicorn/smackchat/src/master/", None, None, "BitBucket"),
    MINUTES_TO_MIDNIGHT: Project(MINUTES_TO_MIDNIGHT, "console timer app", ["C++", "threads"], "https://github.com/JoJaJones/MinutesToMidnight", "https://repl.it/@JoJaJones/MinutesToMidnight", "repl.it"),
    CA_RULES: Project(CA_RULES, "elementary cellular automata generator", ["Python"], "https://github.com/JoJaJones/ElementaryCellularAutomata", "https://repl.it/@JoJaJones/CARules", "repl.it"),
    FAST_SQRT: Project(FAST_SQRT, "fast square root approximator", ["C++"], "https://github.com/JoJaJones/FastSquareRoot")
}

PROJECT_TITLE_LIST = []
for item in PROJECT_DICT:
    PROJECT_TITLE_LIST.append(item)
PROJECT_TITLE_LIST.sort()

