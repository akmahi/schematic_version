from omniparser.parser import OmniParser

schema_file_path = "../schemas/baco_hap/provider_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/baco_hap/practice_provider.txt", "outputs/baco_hap/practice_provider.json")