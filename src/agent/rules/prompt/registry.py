from agent.rules.prompt.pr001 import PR001
from agent.rules.prompt.pr002 import PR002


def get_prompt_rules():
    return [
        PR001(),
        PR002(),
    ]
