"""Unit tests for shared base error classes."""

from cognitive_shield.shared.errors.base_errors import (
    CognitiveShieldError,
    ContractValidationError,
    PipelineConfigurationError,
)


def test_contract_validation_error_inherits_from_cognitive_shield_error() -> None:
    """ContractValidationError is part of the Cognitive Shield error hierarchy."""
    error = ContractValidationError("invalid contract")

    assert isinstance(error, CognitiveShieldError)
    assert isinstance(error, Exception)
    assert str(error) == "invalid contract"


def test_pipeline_configuration_error_inherits_from_cognitive_shield_error() -> None:
    """PipelineConfigurationError is part of the Cognitive Shield error hierarchy."""
    error = PipelineConfigurationError("invalid pipeline configuration")

    assert isinstance(error, CognitiveShieldError)
    assert isinstance(error, Exception)
    assert str(error) == "invalid pipeline configuration"
