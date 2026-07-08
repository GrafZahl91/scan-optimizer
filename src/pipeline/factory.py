from logger import LOGGER

from pipeline.archive import ArchiveStep
from pipeline.convert import ConvertStep
from pipeline.cleanup import CleanupStep
from pipeline.enhance import EnhanceStep
from pipeline.ocr_preprocess import OCRPreprocessStep
from pipeline.deskew import DeskewStep
from pipeline.border import BorderRemovalStep
from pipeline.blank_pages import BlankPageStep
from pipeline.rebuild import RebuildStep


class PipelineFactory:
    @staticmethod
    def build(doc_type, profile):
        LOGGER.info(
            f"Pipeline: Dokumenttyp={doc_type}, Profil={profile}"
        )

        if doc_type == "DIGITAL":
            return []

        return [
            ArchiveStep(),
            ConvertStep(),
            CleanupStep(),
            EnhanceStep(),
            DeskewStep(),
            BorderRemovalStep(),
            BlankPageStep(),
            OCRPreprocessStep(),
            RebuildStep(),
        ]
