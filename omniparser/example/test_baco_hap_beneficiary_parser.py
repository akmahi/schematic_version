from omniparser.parser import OmniParser

schema_file_path = "../schemas/baco_hap/beneficiary_config_new.json"


parser = OmniParser(schema_file_path)
parser.transform("data/baco_hap/beneficiary.txt", "outputs/baco_hap/beneficiary.json")