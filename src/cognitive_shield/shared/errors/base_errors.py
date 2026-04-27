"""
Shared base error classes for Sprint 0.
"""


class CognitiveShieldError(Exception):
    """
    Base exception for the Cognitive Shield repository.
    """


class ContractValidationError(CognitiveShieldError):
    """
    Raised when a shared contract is structurally invalid.
    """


class PipelineConfigurationError(CognitiveShieldError):
    """
    Raised when a Sprint 0 pipeline shell is misconfigured.
    """
