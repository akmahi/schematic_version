from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/gi/allergy_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/gi/allergy.csv", "outputs/gi/allergy.json")