from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/837/claim_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/837/837_original.txt", "outputs/837/837_original.json")