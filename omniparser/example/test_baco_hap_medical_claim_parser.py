from omniparser.parser import OmniParser

schema_file_path = "../schemas/baco_hap/medical_claim_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/baco_hap/medical_claim.txt", "outputs/baco_hap/medical_claim.json")