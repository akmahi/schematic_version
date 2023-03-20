from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/provider_roster/provider_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/provider_roster/provider_roster.txt", "outputs/provider_roster/provider_roster.json")