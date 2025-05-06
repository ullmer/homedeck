from enum import Enum


class ButtonElementAction(Enum):
    PAGE_BACK = '$page.back'
    PAGE_PREVIOUS = '$page.previous'
    PAGE_NEXT = '$page.next'
    PAGE_GO_TO = '$page.go_to'


class InteractionType(Enum):
    TAP = 'tap'
    HOLD = 'hold'


class IconSource(Enum):
    BLANK = 'blank'
    LOCAL = 'local'
    URL = 'url'
    TEXT = 'text'
    MATERIAL_DESIGN = 'mdi'
    PHOSPHOR = 'pi'


class PhosphorIconVariant:
    THIN = 'thin'
    LIGHT = 'light'
    REGULAR = 'regular'
    BOLD = 'bold'
    FILL = 'fill'
    DUOTONE = 'duotone'


class SleepStatus:
    WAKE = 'wake'
    DIM = 'dim'
    SLEEP = 'sleep'
