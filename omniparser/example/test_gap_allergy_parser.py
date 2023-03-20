from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/gap/allergy_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/gap/allergy.csv", "outputs/gap/allergy.json")