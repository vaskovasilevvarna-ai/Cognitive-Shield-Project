"""
Shared base error classes for Cognitive Shield.
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
    Raised when a pipeline shell is misconfigured.
    """
