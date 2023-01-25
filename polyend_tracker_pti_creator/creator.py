from polyend_tracker_pti_creator.utils.args import parse_args
from polyend_tracker_pti_creator.utils.settings import Settings
from polyend_tracker_pti_creator.utils.pti.pti import PTI


def main():
    args = parse_args()
    settings = Settings(args)
    create(settings.settings)


def create(settings):
    pti = PTI(settings)
    pti.create()
    print("Success! new pti file(s) have been saved to " + settings['files'][0]['destination_path'] + ".")
