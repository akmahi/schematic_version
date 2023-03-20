from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/cclf/cclf8_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/cclf/cclf8.txt", "outputs/cclf/cclf8.json")

# S3 example
# parser.transform("s3://sureshn-hec-landing-bucket/cclf8.txt", "s3://sureshn-hec-landing-bucket/cclf8.json")
