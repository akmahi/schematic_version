from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/practice_roster/practice_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/practice_roster/practice_roster.txt", "outputs/practice_roster/practice_roster.json")