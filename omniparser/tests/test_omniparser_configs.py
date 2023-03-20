import os
import json
import pytest
from pathlib import Path
from omniparser.parser import OmniParser

ACTUAL_OUTPUTS_DIR = "tests/actual_outputs"


class TestOmniParserConfigs:

    test_cases = [
        (
            "schemas/healthec/practice_roster/practice_config.json",
            "tests/data/practice_roster/practice_roster.txt",
            "tests/expected_outputs/practice_roster/practice_roster.json",
        ),
        (
            "schemas/healthec/provider_roster/provider_config.json",
            "tests/data/provider_roster/provider_roster.txt",
            "tests/expected_outputs/provider_roster/provider_roster.json",
        ),
        (
            "schemas/healthec/837/claim_config.json",
            "tests/data/837/837_original.txt",
            "tests/expected_outputs/837/837_original.json",
        ),
        (
            "schemas/healthec/cclf/cclf8_config.json",
            "tests/data/cclf/cclf8.txt",
            "tests/expected_outputs/cclf/cclf8.json",
        ),
        (
            "schemas/baco_hap/beneficiary_config.json",
            "tests/data/baco_hap/beneficiary.txt",
            "tests/expected_outputs/baco_hap/beneficiary.json",
        ),
        (
            "schemas/baco_hap/provider_config.json",
            "tests/data/baco_hap/practice_provider.txt",
            "tests/expected_outputs/baco_hap/practice_provider.json",
        ),
        (
            "schemas/baco_hap/medical_claim_config.json",
            "tests/data/baco_hap/medical_claim.txt",
            "tests/expected_outputs/baco_hap/medical_claim.json",
        ),
        (
            "schemas/healthec/ecw/allergy_config.json",
            "tests/data/ecw/allergy.txt",
            "tests/expected_outputs/ecw/allergy.json",
        ),
        (
            "schemas/healthec/ecw/diagnosis_config.json",
            "tests/data/ecw/diagnosis.txt",
            "tests/expected_outputs/ecw/diagnosis.json",
        ),
        (
            "schemas/healthec/ecw/encounter_config.json",
            "tests/data/ecw/encounter.txt",
            "tests/expected_outputs/ecw/encounter.json",
        ),
        (
            "schemas/healthec/ecw/examination_config.json",
            "tests/data/ecw/examination.txt",
            "tests/expected_outputs/ecw/examination.json",
        ),
        (
            "schemas/healthec/ecw/facility_config.json",
            "tests/data/ecw/facility.txt",
            "tests/expected_outputs/ecw/facility.json",
        ),
        (
            "schemas/healthec/ecw/family_history_config.json",
            "tests/data/ecw/familyhistory.txt",
            "tests/expected_outputs/ecw/familyhistory.json",
        ),
        (
            "schemas/healthec/ecw/hospitalization_config.json",
            "tests/data/ecw/hospitalization.txt",
            "tests/expected_outputs/ecw/hospitalization.json",
        ),
        (
            "schemas/healthec/ecw/hpi_config.json",
            "tests/data/ecw/hpi.txt",
            "tests/expected_outputs/ecw/hpi.json",
        ),
        (
            "schemas/healthec/ecw/immunization_config.json",
            "tests/data/ecw/immunization.txt",
            "tests/expected_outputs/ecw/immunization.json",
        ),
        (
            "schemas/healthec/ecw/medical_history_config.json",
            "tests/data/ecw/medicalhistory.txt",
            "tests/expected_outputs/ecw/medicalhistory.json",
        ),
        (
            "schemas/healthec/ecw/medication_config.json",
            "tests/data/ecw/medication.txt",
            "tests/expected_outputs/ecw/medication.json",
        ),
        (
            "schemas/healthec/ecw/obgyn_history_config.json",
            "tests/data/ecw/obgynhistory.txt",
            "tests/expected_outputs/ecw/obgynhistory.json",
        ),
        (
            "schemas/healthec/ecw/order_and_result_config.json",
            "tests/data/ecw/orderandresult.txt",
            "tests/expected_outputs/ecw/orderandresult.json",
        ),
        (
            "schemas/healthec/ecw/patient_demographic_config.json",
            "tests/data/ecw/patientdemographic.txt",
            "tests/expected_outputs/ecw/patientdemographic.json",
        ),
        (
            "schemas/healthec/ecw/physical_exam_config.json",
            "tests/data/ecw/physicalexam.txt",
            "tests/expected_outputs/ecw/physicalexam.json",
        ),
        (
            "schemas/healthec/ecw/practice_user_config.json",
            "tests/data/ecw/practiceuser.txt",
            "tests/expected_outputs/ecw/practiceuser.json",
        ),
        (
            "schemas/healthec/ecw/preventive_config.json",
            "tests/data/ecw/preventive.txt",
            "tests/expected_outputs/ecw/preventive.json",
        ),
        (
            "schemas/healthec/ecw/problem_list_config.json",
            "tests/data/ecw/problemlist.txt",
            "tests/expected_outputs/ecw/problemlist.json",
        ),
        (
            "schemas/healthec/ecw/procedure_config.json",
            "tests/data/ecw/procedure.txt",
            "tests/expected_outputs/ecw/procedure.json",
        ),
        (
            "schemas/healthec/ecw/procedure_code_config.json",
            "tests/data/ecw/procedurecode.txt",
            "tests/expected_outputs/ecw/procedurecode.json",
        ),
        (
            "schemas/healthec/ecw/referral_config.json",
            "tests/data/ecw/referral.txt",
            "tests/expected_outputs/ecw/referral.json",
        ),
        (
            "schemas/healthec/ecw/social_history_config.json",
            "tests/data/ecw/socialhistory.txt",
            "tests/expected_outputs/ecw/socialhistory.json",
        ),
        (
            "schemas/healthec/ecw/surgical_history_config.json",
            "tests/data/ecw/surgicalhistory.txt",
            "tests/expected_outputs/ecw/surgicalhistory.json",
        ),
        (
            "schemas/healthec/ecw/vital_config.json",
            "tests/data/ecw/vital.txt",
            "tests/expected_outputs/ecw/vital.json",
        ),
        (
            "schemas/healthec/qrda/clinical_config.json",
            "tests/data/qrda/qrda.json",
            "tests/expected_outputs/qrda/qrda.json",
        ),
        (
            "schemas/healthec/gap/allergy_config.json",
            "tests/data/gap/allergy.csv",
            "tests/expected_outputs/gap/allergy.json",
        ),
        (
            "schemas/healthec/gap/care_config.json",
            "tests/data/gap/care.csv",
            "tests/expected_outputs/gap/care.json",
        ),
        (
            "schemas/healthec/gap/immunization_config.json",
            "tests/data/gap/immunization.csv",
            "tests/expected_outputs/gap/immunization.json",
        ),
        (
            "schemas/healthec/gap/vital_config.json",
            "tests/data/gap/vital.csv",
            "tests/expected_outputs/gap/vital.json",
        ),
        (
            "schemas/healthec/gi/allergy_config.json",
            "tests/data/gi/allergy.csv",
            "tests/expected_outputs/gi/allergy.json",
        ),
        (
            "schemas/healthec/gi/demographic_config.json",
            "tests/data/gi/demographic.csv",
            "tests/expected_outputs/gi/demographic.json",
        ),
        (
            "schemas/healthec/gi/medical_condition_config.json",
            "tests/data/gi/medicalcondition.csv",
            "tests/expected_outputs/gi/medicalcondition.json",
        ),
        (
            "schemas/healthec/gi/smoking_config.json",
            "tests/data/gi/smoking.csv",
            "tests/expected_outputs/gi/smoking.json",
        ),
    ]

    @classmethod
    def setup_method(cls):
        if not os.path.exists(ACTUAL_OUTPUTS_DIR):
            os.mkdir(ACTUAL_OUTPUTS_DIR)

    @pytest.mark.parametrize("schema, test_data_fp, expected_output_fp", test_cases)
    def test_omniparser_configs(self, schema, test_data_fp, expected_output_fp):
        test_data_path = Path(test_data_fp)
        actual_output_fp = os.path.join(ACTUAL_OUTPUTS_DIR, test_data_path.name + ".json")
        try:
            parser = OmniParser(schema)
            parser.transform(test_data_fp, actual_output_fp)

            actual_output = json.load(open(actual_output_fp))
            expected_output = json.load(open(expected_output_fp))
            assert actual_output == expected_output
        finally:
            os.remove(actual_output_fp)
