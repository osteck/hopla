from enum import Enum


class Signals(Enum):
    DOCUMENT_CREATED = "DOCUMENT_CREATED"
    DOCUMENT_VALIDATED = "DOCUMENT_VALIDATED"
    DOCUMENT_CLONED = "DOCUMENT_CLONED"
    EXCEPTION_RAISED = "EXCEPTION_RAISED"
    WARNING_RAISED = "WARNING_RAISED"
