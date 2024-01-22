from src.MoviesRecom.config.configuration import ConfigurationManager
from src.MoviesRecom.components.data_transformation import DataTransformation
from src.MoviesRecom.logging import logger


STAGE_NAME = 'Data Transformation'


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transofrmation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.prepare_data()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
