from omniparser.parser import OmniParser

schema_file_path = "../schemas/healthec/ecw/patient_demographic_config.json"


parser = OmniParser(schema_file_path)
parser.transform("data/ecw/patientdemographic.txt", "outputs/ecw/patientdemographic.json")